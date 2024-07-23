from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pymongo import MongoClient
import gridfs
from werkzeug.utils import secure_filename
import os
from bson import ObjectId
from io import BytesIO
from pathlib import Path

app = Flask(__name__)
cors = CORS()
cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

# 初始化数据库
client = MongoClient('localhost', 27017)
db = client['image_database']
fs = gridfs.GridFS(db)

# 设置上传文件的保存路径
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/api/upload', methods=['POST'])
def upload():
    # 获取文件
    file = next(iter(request.files.values()))
    # 获取文件名
    filename = secure_filename(file.filename)
    # 获取文件路径
    file_path = Path(app.config['UPLOAD_FOLDER']) / filename

    print(f"POST: 图片 \"{file.filename}\"上传成功!")

    # 将上传文件保存到本地
    file.save(file_path)
    # 获取文件大小
    file_size = os.path.getsize(file_path)
    # 将本地文件保存到数据库
    with open(file_path, 'rb') as f:
        file_id = fs.put(f, filename=filename)
    # 删除本地保存的文件
    os.remove(file_path)

    # 返回信息
    file_info = {
        'file_id': str(file_id),
        'filename': filename,
        'size': file_size,
        'content_type': file.content_type
    }
    return jsonify(file_info), 200


@app.route('/api/images', methods=['GET'])
def list_images():
    files = fs.find()
    image_list = [{'id': str(file._id), 'filename': file.filename} for file in files]
    return jsonify(image_list)


@app.route('/api/images/<image_id>', methods=['GET'])
def get_image(image_id):
    image = fs.get(ObjectId(image_id))
    return send_file(BytesIO(image.read()), download_name=image_id + '.jpg', mimetype=image.content_type)


if __name__ == '__main__':
    app.run(debug=True)
