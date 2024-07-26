from pymongo import MongoClient
import gridfs

client = MongoClient('localhost', 27017)
db = client['bakabooru']
db_fs = gridfs.GridFS(db)
db_ImageGallery = db['ImageGallery']
