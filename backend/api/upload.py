from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from backend.db import db_fs, db_ImageGallery, get_sequence
from pathlib import Path
from PIL import Image
import os

upload_bp = Blueprint('upload', __name__, url_prefix='/api')

# 设置上传文件的保存路径
CACHE_FOLDER = 'Cache'
if not os.path.exists(CACHE_FOLDER):
    os.makedirs(CACHE_FOLDER)


def get_thumbnail_file(original_file_path, thumbnail_image_path, width, height):
    # 打开原始图片
    with Image.open(original_file_path) as img:
        # 获取图片的宽度和高度
        img_width, img_height = img.size

        # 裁剪图片
        if img_width >= img_height:
            left = (img_width - img_height * width / height) / 2
            top = 0
            right = (img_width + img_height * width / height) / 2
            bottom = img_height
        else:
            left = 0
            top = (img_height - img_width * height / width) / 2
            right = img_width
            bottom = (img_height + img_width * height / width) / 2
        img = img.crop((left, top, right, bottom))

        # 缩小图片并保存图片
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.save(thumbnail_image_path)


@upload_bp.route('/upload', methods=['POST'])
def upload():
    # 获取文件缓存
    file = next(iter(request.files.values()))
    filename = secure_filename(file.filename)
    original_file_path = Path(CACHE_FOLDER) / filename
    file.save(original_file_path)

    # 生成图集ID
    set_id = str(get_sequence('set_id'))

    # 生成缩略图
    thumbnail_image_path = Path(CACHE_FOLDER) / f"{set_id} -thumbnail 300x420{Path(filename).suffix}"
    get_thumbnail_file(original_file_path, thumbnail_image_path, 300, 420)

    # 将文件存入数据库
    with open(original_file_path, 'rb') as f:
        original_file_id = str(db_fs.put(f, filename=filename))
    with open(thumbnail_image_path, 'rb') as f:
        thumbnail_file_id = str(db_fs.put(f, filename=thumbnail_image_path.name))

    # 删除缓存文件
    os.remove(original_file_path)
    os.remove(thumbnail_image_path)

    # 保存图集信息
    ImageSet_info = {
        'id': set_id,
        "thumbnail_images": {
            'file_id': thumbnail_file_id,
            'file_name': thumbnail_image_path.name,
            'width': 300,
            'height': 420,
        },
        "original_images": {
            "0": {
                'file_id': original_file_id,
                'file_name': filename,
                'content_type': file.content_type
            }
        }
    }
    db_ImageGallery.insert_one(ImageSet_info)

    print(f"[后台] POST: 图片\"{file.filename}\"上传成功。(set_id:{set_id})")

    return jsonify({"group_id": original_file_id}), 200
