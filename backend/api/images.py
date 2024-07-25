from flask import Blueprint, jsonify, send_file
from backend.db import fs
from bson import ObjectId
from io import BytesIO

images_bp = Blueprint('images', __name__, url_prefix='/api')


@images_bp.route('/images', methods=['GET'])
def list_images():
    files = fs.find()
    image_list = [{'id': str(file._id), 'filename': file.filename} for file in files]

    print(f"[后台] GET: 成功获取 {len(image_list)} 个图集信息。")

    return jsonify(image_list)


@images_bp.route('/images/<image_id>', methods=['GET'])
def get_image(image_id):
    image = fs.get(ObjectId(image_id))
    return send_file(BytesIO(image.read()), download_name=image_id + '.jpg', mimetype=image.content_type)
