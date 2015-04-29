from flask import *


#!/usr/bin/python

# Copyright (c) 2015 ObjectLabs Corporation
# Distributed under the MIT license - http://opensource.org/licenses/MIT

__author__ = 'mongolab'

# Written with pymongo-2.6
# Documentation: http://api.mongodb.org/python/
# A python script connecting to a MongoDB given a MongoDB Connection URI.

import sys
import pymongo

from bson import Binary, Code
from bson import json_util
from bson.json_util import dumps

### Create seed data

app=Flask(__name__)

MONGODB_URI = 'mongodb://heroku_app35358178:cld5pedb57lkvl6fj1af5ogvb3@ds035027.mongolab.com:35027/heroku_app35358178'
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

total_ids=0

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

###############################################################################
# main
###############################################################################

def main(args):
    global total_ids
    total_ids = 0
    app.run(debug=True, port=8000)
    client.close()

@app.route("/index", methods=['GET'])
@app.route("/", methods =['GET'])
@app.route("/login", methods =['GET'])

def index():
    return render_template('newlogin.html')

@app.route("/createGroup", methods=['GET'])

def create_group():
    global total_ids
    username = request.args.get('user')
    total_ids += 1
    db["users"].update(
    { "username": username },
    { "$addToSet":{"groups": str(total_ids)} },
    upsert=True)
    return str(total_ids)

@app.route("/foodlist", methods = ['GET','POST'])

def return_foodlist():
    foods = db['foods']
    group_id = request.args.get('group_id')
    if request.method == 'GET':
        food_list = foods.find({'group_id': group_id}).sort('_id',pymongo.ASCENDING)
        return dumps(food_list)
    elif request.method == 'POST':
        foods.insert({'group_id' : group_id, 'username' : request.form['username'], 'ingredient': request.form['ingredient'], 'amount': request.form['amount']} )
        return "success"


@app.route("/plan", methods=['GET'])

def return_planner():
    return render_template('meal_planner.html')

"""Sylvie: The following Code adds a html file to the server"""
@app.route("/userprofile")

def return_user_prof():
    return render_template('userprofile.html')

@app.route("/userinfo.json", methods=['GET'])

def user_info():
    users = db['users']
    username = request.args.get('username')
    cursor = users.find({'username': username})
    return dumps(cursor)

@app.route("/sendUserInfo", methods=['POST'])

def sendUser():
    users = db['users']
    username = request.form['username']
    diet_restrict = request.form['dietrestrict']
    group_ids = request.form['group_ids']
    users.update({'username': username},{'username': username, 'diet_restrict': diet_restrict, 'group_ids': group_ids},  upsert=True)
    cursor = users.find_one({'username':username})
    return dumps(cursor)

@app.route("/fblogin", methods =['GET'])

def facebook():
    return render_template('fbapi.html')

@app.route("/<arg>")

def args(arg=None):
    return arg

if __name__ == '__main__':
        main(sys.argv[1:])
