""" Flask configuration to connect to the database """
from flask_pymongo import pymongo
import os

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

client = pymongo.MongoClient(f"mongodb+srv://dbPaulina:paulinatb@example.ekebt.mongodb.net/db_example?retryWrites=true&w=majority")

db = client.db_example
