from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
import db_config as database

#RESOURCES
from res.badge import Badge
from res.badges import Badges
from res.posts import Posts

app=Flask(__name__)
api=Api(app)

@app.route('/all/adults/')
def get_adults():
    response = list(database.db.Badges.find({'age': {"$gte": 18}}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/projection/')
def get_name_and_age():
    response = list(database.db.Badges.find({'age': {"$gte": 18}}, {'name': 1, 'age':1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/kids/')
def get_kids():
    response = list(database.db.Badges.find({'age': {"$lt": 18}}, {'name': 1, 'age':1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/user_names/')
def get_all_names():
    response = list(database.db.Badges.find({},{'name':1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

api.add_resource(Badge,'/new/','/<string:by>:<string:data>/')
api.add_resource(Badges, '/all/', '/delete/all/')
api.add_resource(Posts, '/new/post/<string:_id>/', '/posts/<string:_id>/', '/<string:_id>/<string:uuid>/')


if __name__ == '__main__':
    app.run(load_dotenv=True)