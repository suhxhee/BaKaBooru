from pymongo import MongoClient
import gridfs

client = MongoClient('localhost', 27017)
db = client['bakabooru']
fs = gridfs.GridFS(db)
images = db['images']
