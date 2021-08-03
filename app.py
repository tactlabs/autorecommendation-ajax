from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
from pymongo import MongoClient
  
app = Flask(__name__)
  
load_dotenv
mongo_uri = os.getenv('MONGO_URI')
cluster = MongoClient(mongo_uri)

db = cluster["recommendation_bar"]

collection = db["list"]
  
@app.route("/", methods=["GET", "POST"])
def home():
    languages_list = []

    if request.method == "GET":
        languages = db.list.find()

        

        for language in languages:
            languages_list.append(language['Name'])

       
    

    return render_template("index.html", language = languages_list)

# @app.route("/", methods=["POST"])
# def func():

        # languages = db.list.distinct("Name")

    



        

        # languages = db.list.find({"Name":{ 
        #         "$regex" : search_word,
        #         '$options' : 'i'
        #     }},{"_id":False})

        # for language in languages:
        #     languages_list.append(language)

        
          
        # return render_template("index1.html")
  
  
if __name__ == '__main__':
    app.run(debug=True)