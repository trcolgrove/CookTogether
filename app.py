from flask import *


#!/usr/bin/python

# Copyright (c) 2015 Thomas Colgrove
# Server and API for COOKTOGETHER (tm)
# written in flask and pymongo, using mongolabs

__author__ = 'mongolab'

import sys
import pymongo
import datetime
import re

from bson import Binary, Code
from bson import json_util
from bson.json_util import dumps

### Create seed data

app=Flask(__name__)

# instantiate the mongoDB_URI
### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
MONGODB_URI = 'mongodb://heroku_app35358178:cld5pedb57lkvl6fj1af5ogvb3@ds035027.mongolab.com:35027/heroku_app35358178'
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()


total_ids=0



###############################################################################
# main: Run the app on port 8000
###############################################################################

def main(args):
    global total_ids
    total_ids = 0
    app.run(debug=True, port=8000)
    client.close()


# Display front-end page for user login
@app.route("/index", methods=['GET'])
@app.route("/", methods =['GET'])
@app.route("/login", methods =['GET'])

def index():
    return render_template('newlogin.html')


# Display front-end page for user profiles
@app.route("/userprofile", methods=['GET'])

def return_user_prof():
    return render_template('userprofile.html')

# Display front-end page for group meal plans
@app.route("/plan", methods=['GET'])

def return_planner():
    return render_template('meal_planner.html')


@app.route("/userinfo.json", methods=['GET'])

def user_info():
    users = db['users']
    user_id = request.args.get('user_id')
    user = users.find_one({'user_id': user_id})
    if user == None:
        return '{}'
    else:
        return dumps(user)

# API Call to request a new group.
# Methods: 'GET', 'POST'
# Args: user_id
# Return: a unique identifier string for the new group_id
# Description: increments the number of total groups, adds the group_id to the
# callee user's 'group' field

@app.route("/createGroup", methods=['GET'])

def create_group():
    global total_ids

    user_id = request.args.get('user_id')
    group_name = request.args.get('group_name')

    group_id = datetime.datetime.now().isoformat()
    group_id = re.sub(r'\W+', '', group_id)

    new_group = {'group_name': group_name, 'group_id':str(group_id)}
    db["users"].update(
    { "user_id": user_id },
    { "$addToSet":{"groups": {'group_name': group_name, 'group_id':str(group_id)}}},
    upsert=True)
    db["groups"].insert( {'group_id' : str(group_id),'group_name' : group_name, 'user_ids': [user_id] })
    return str(group_id)

@app.route("/addfriends", methods=['GET'])

def add_friend():
    return render_template('addfriends.html')

@app.route("/addUserToGroup", methods=['POST'])

def addUser():
    user_id = request.form.get('user_id')
    group_id = request.form.get('group_id')


    group_name = db["groups"].find_one({'group_id':group_id})['group_name']

    db["groups"].update(
    { "group_id": group_id },
    { "$addToSet":{"user_ids": user_id }},
    upsert=True)

    db["users"].update(
    { "user_id": user_id },
    { "$addToSet":{"groups": {'group_name': group_name, 'group_id':str(group_id)}}},
    upsert=True)
    return "success"



@app.route("/groupinfo.json")

def get_group_info():
    groups = db['groups']
    group_id = request.args.get("group_id")
    group = groups.find_one({"group_id" : group_id})
    print group
    return dumps(group)

# API Call to handle changes in group foodlist/mealplanner data
# Methods: 'GET', 'POST'
# Args (GET, POST): group_id, user_id
# Form (POST-ONLY): JSON document containing the fields username
# ingredient, and ammount

@app.route("/foodlist", methods = ['GET','POST'])

def return_foodlist():
    foods = db['foods']
    group_id = request.args.get('group_id')
    user_id = request.args.get('user_id')
    if request.method == 'GET':
        food_list = foods.find({'group_id': group_id}).sort('_id',pymongo.ASCENDING)
        return dumps(food_list)
    elif request.method == 'POST':
        foods.insert({'group_id' : group_id, 'username' : request.form['username'], 'ingredient': request.form['ingredient'], 'amount': request.form['amount']})
        return "success"


# API Call to handle changes and creation of user information
# Methods: 'POST'
# Args (GET, POST): group_id, user_id
# Form (POST-ONLY): JSON document containing the fields username
# ingredient, and ammount

@app.route("/sendUserInfo", methods=['POST'])

def sendUser():
    users = db['users']

    data = request.json

    username = data['username']
    diet_restrict = data['diet_restrict']
    groups = data['groups']
    friends = data['friends']
    user_id = data['user_id']

    print user_id
    #if user_id == None or username == None or diet_restrict == None or groups == None or friends == None:
    #    return "{error : whoops!, something is wrong with your data!}"
    users.update({'username': username},{'username': username, 'diet_restrict': diet_restrict, 'groups': groups, 'friends': friends, 'user_id': user_id },  upsert=True)
    cursor = users.find_one({'username':username})
    return dumps(cursor)


@app.route("/newuser")

def newUserPage():
    return render_template('newuser.html')

@app.route("/fblogin", methods =['GET'])

def facebook():
    return render_template('fbapi.html')

@app.route("/<arg>")

def args(arg=None):
    return arg

if __name__ == '__main__':
        main(sys.argv[1:])
