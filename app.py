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

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname


###############################################################################
# main
###############################################################################

def main(args):

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

    app.run()


    client.close()




@app.route("/index", methods=['GET'])
@app.route("/", methods =['GET'])


def index():
    return render_template('index.html')


@app.route("/foodlist", methods = ['GET','POST'])

def return_foodlist():
    foods = db['foods']
    meal_id = request.args.get('meal_id')
    if request.method == 'GET':
        cursor = (foods.find({'meal_id': meal_id}))
        return dumps(cursor)
    elif request.method == 'POST':
        foods.insert({'meal_id' : meal_id, 'username' : request.form['username'], 'ingredient': request.form['ingredient'], 'amount': request.form['amount']} )
        return "success"

@app.route("/<arg>")

def args(arg=None):
    return arg

if __name__ == '__main__':
        main(sys.argv[1:])
