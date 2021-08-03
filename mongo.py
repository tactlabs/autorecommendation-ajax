from flask import Flask,render_template,request,redirect,session,jsonify,url_for,flash
from dotenv import load_dotenv

import os
from pymongo import MongoClient


app=Flask(__name__)
app.config['SECRET_KEY'] = '4aad4c8ec9d4fe4f72aab7ff4e82cc58'


load_dotenv
mongo_uri = os.getenv('MONGO_URI')
cluster = MongoClient(mongo_uri)

db = cluster["recommendation_bar"]

collection = db["list"]

@app.route('/',methods=['GET','POST'])
def login_page():
    list = [
    {"Name" :"Afghanistan"},
    {"Name" :"Albania"},
    {"Name" :"Barbuda"},
    {"Name" :"Belgium"},
    {"Name" :"China"},
    {"Name" :"Cameron"},
    {"Name" :"Denmark"},
    {"Name" :"Island"},
    {"Name" :"India"},
    {"Name" :"Costa Rica"},
    {"Name" :"Mauritania"},
    {"Name" :"Madagascar"},
    {"Name" :"Mnali"},
    {"Name" :"Malta"}

]
    collection.insert_many(list)

    return "successfull!"


if __name__ == '__main__':
    app.run(debug=True)