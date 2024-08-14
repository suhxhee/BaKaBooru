from flask import Blueprint, jsonify, send_file
from backend.db import db_fs, db_ImageGallery
from bson import ObjectId
from io import BytesIO

gallery_bp = Blueprint('gallery', __name__, url_prefix='/api')


@gallery_bp.route('/gallery', methods=['GET'])
def gallery():
    ImageGallery = db_ImageGallery.find()
    ImageGallery_info = [{'id': ImageSet.get('id')} for ImageSet in ImageGallery]

    print(f"[后台] GET: 成功获取{len(ImageGallery_info)}个图集信息。")

    return jsonify(ImageGallery_info)


@gallery_bp.route('/set/<set_id>/thumbnail', methods=['GET'])
def get_thumbnail(set_id):
    result = db_ImageGallery.find_one({'id': set_id})
    if not result:
        return "Set not found", 404

    print(f"[后台] GET: 成功获取缩略图(set_id:{set_id})。")

    image = result.get('thumbnail_images')
    image_file = db_fs.get(ObjectId(image['file_id']))
    return send_file(
        BytesIO(image_file.read()),
        download_name=image['file_name'],
        mimetype=image_file.content_type
    )


@gallery_bp.route('/set/<set_id>/image/<image_id>', methods=['GET'])
def get_image(set_id, image_id):
    result = db_ImageGallery.find_one({'id': set_id})
    if not result:
        return "Set not found", 404

    print(f"[后台] GET: 成功获取原图(set_id:{set_id},image_id:{image_id})。")

    image = result.get("original_images")[image_id]
    image_file = db_fs.get(ObjectId(image.get('file_id')))
    return send_file(
        BytesIO(image_file.read()),
        download_name=image.get('file_name'),
        mimetype=image_file.content_type
    )
