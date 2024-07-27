from pymongo import MongoClient,ReturnDocument
import gridfs

# 初始化数据库
client = MongoClient('localhost', 27017)
db = client['bakabooru']

# 初始化图片数据库
db_fs = gridfs.GridFS(db)
db_ImageGallery = db['ImageGallery']

# 初始化计数器
db_Counters = db['IDCounters']
# 初始化set_id计数器
if db_Counters.count_documents({"_id": "set_id"}) == 0:
    db_Counters.insert_one({"_id": "set_id", "seq": -1})


# 计数器函数
def get_sequence(name):
    counter = db_Counters.find_one_and_update(
        {'_id': name},
        {'$inc': {'seq': 1}},
        return_document=ReturnDocument.AFTER,
        upsert=True
    )
    return counter['seq']
