from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
db_client = MongoClient("mongodb://db:27017/")
db = db_client["mydatabase"]

@app.route('/')
def index():
    return "<h1>YESHWANTH I-2022BCD0055</h1><p>This is a microservices application using Docker with MongoDB for assignment.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
