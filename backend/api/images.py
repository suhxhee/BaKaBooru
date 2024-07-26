from flask import Blueprint, jsonify, send_file
from backend.db import db_fs, db_gallery
from bson import ObjectId
from io import BytesIO

images_bp = Blueprint('images', __name__, url_prefix='/api')


@images_bp.route('/gallery', methods=['GET'])
def list_images():
    files = db_fs.find()
    image_list = [{'id': str(file._id), 'filename': file.filename} for file in files]

    print(f"[后台] GET: 成功获取 {len(image_list)} 个图集信息。")

    return jsonify(image_list)


@images_bp.route('/set/<set_id>', methods=['GET'])
def get_image(set_id):
    image = db_fs.get(ObjectId(set_id))
    return send_file(BytesIO(image.read()), download_name=set_id + '.jpg', mimetype=image.content_type)
