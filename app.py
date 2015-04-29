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
    # First we'll add a few songs. Nothing is required to create the songs
    # collection; it is created automatically when we insert.

    foods = db['foods']

    # Note that the insert method can take either an array or a single dict.

    # Then we need to give Boyz II Men credit for their contribution to
    # the hit "One Sweet Day".

    #query = {'song': 'One Sweet Day'}

    #song.update(query, {'$set': {'artist': 'Mariah Carey ft. Boyz II Men'}})

    # Finally we run a query which returns all the hits that spent 10 or
    # more weeks at number 1.

    #cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)

    ### Since this is an example, we'll clean up after ourselves.

    ### Only close the connection when your app is terminating

    app.run(debug=True, port=33507)


    client.close()

@app.route("/index", methods=['GET'])
@app.route("/", methods =['GET'])

def index():
    return render_template('index.html')

@app.route("/createGroup", methods=['GET'])

def create_group():
    global total_ids
    username = request.args.get('user')
    total_ids += 1
    db["users"].update(
    { "username": username },
    { "$addToSet":{"groups": total_ids} },
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


@app.route("/dietrestrict", methods=['POST'])

def edit_diet():
    user = request.args.get('user_id')
    diet = request.args.get('diet')

    users = db['users']
    """users.find_one_and_update({'userid' : userid}, {}"""
    return "success"


"""Sylvie: The following Code adds a html file to the server"""
@app.route("/userprofile")

def return_user_prof():
    return render_template('userprofile.html')

@app.route("/getUserInfo", methods=['GET'])

def getUserInfo():
    users = db['users']
    request.args.get('user_id')
    users.insert({"username":username})
    cursor = users.find()
    return dumps(cursor)

@app.route("/userinfo.json", methods=['GET'])

def user_info():
    username = request.args.get('username')
    user_info = db['users'].find_one({"username": username})
    return user_info

@app.route("/fblogin", methods =['GET'])

def facebook():
    return render_template('fbapi.html')

@app.route("/<arg>")

def args(arg=None):
    return arg

if __name__ == '__main__':
        main(sys.argv[1:])
