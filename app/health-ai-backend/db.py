# db.py
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()  # loads variables from .env

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "health_ai")

if not MONGO_URI:
    raise EnvironmentError("MONGO_URI not set in .env")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

print("✅ Connected to MongoDB Atlas:", DB_NAME)
