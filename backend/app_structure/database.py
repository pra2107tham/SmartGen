from pymongo import MongoClient
import certifi

# MongoDB connection
MONGO_URI = "mongodb+srv://pratham:pratham@smartgen.xp4k1.mongodb.net/smartgen"
mongo_client = MongoClient(MONGO_URI,tlsCAFile=certifi.where())
db = mongo_client.smartgen  # Replace `smartgen` with your database name
