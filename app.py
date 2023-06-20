from pymongo import MongoClient
import gridfs
from datetime import datetime

CONNECTION_STRING = "mongodb://admin:admin@localhost"


def get_db_connection():
    client = MongoClient(CONNECTION_STRING)
    return client


db_conn = get_db_connection()
db_poc = db_conn.poc
fs = gridfs.GridFS(db_poc)

# List DBs
all_dbs = db_conn.list_database_names()
print(all_dbs)

# List Collections in DB
all_collections = db_poc.list_collection_names()
print(all_collections)

# Store a .wav file
TARGET_FOLDER = "input"
TARGET_FILE = "file_example_WAV_1MG.wav"
b = fs.put(
    open(TARGET_FOLDER + "/" + TARGET_FILE, "rb"),
    filename=TARGET_FILE,
    time=datetime.now(),
)

# Fetch the inserted file
out = fs.get(b)
print(out.filename)
print(out.time)
