from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from pathlib import Path
import os
from backend.db import fs, images

upload_bp = Blueprint('upload', __name__, url_prefix='/api')

# 设置上传文件的保存路径
CACHE_FOLDER = 'Cache'
if not os.path.exists(CACHE_FOLDER):
    os.makedirs(CACHE_FOLDER)

@upload_bp.route('/upload', methods=['POST'])
def upload():
    # 获取文件缓存
    file = next(iter(request.files.values()))
    filename = secure_filename(file.filename)
    cache_path = Path(CACHE_FOLDER) / filename
    file.save(cache_path)

    # 将文件存入数据库
    with open(cache_path, 'rb') as f:
        file_id = fs.put(f, filename=filename)
    os.remove(cache_path)

    set_id = images.count_documents({})

    set_info = {
        "set_id": set_id,
        "original_image": {
            "file_id": str(file_id),
            "filename": filename,
            'content_type': file.content_type
        }
    }
    images.insert_one(set_info)

    print(f"[后台] POST: \"{file.filename}\"上传成功，图集ID: {images_id}。")

    return jsonify({"group_id": images_id}), 200
