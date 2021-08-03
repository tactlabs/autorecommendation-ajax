from flask import Flask,render_template,redirect,request,json
from dotenv import load_dotenv
import os
from pymongo import MongoClient


app = Flask(__name__)

load_dotenv
mongo_uri = os.getenv('MONGO_URI')
cluster = MongoClient(mongo_uri)

db = cluster["autorecommendation"]

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


@app.route('/ajaxautocomplete',methods=['POST', 'GET'])
def ajaxautocomplete():
    if request.method=='POST':
        
        result = collection.find()
        print(result)
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)