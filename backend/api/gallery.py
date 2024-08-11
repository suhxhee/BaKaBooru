from flask import Blueprint, jsonify, send_file
from backend.db import db_fs, db_ImageGallery
from bson import ObjectId
from io import BytesIO

gallery_bp = Blueprint('gallery', __name__, url_prefix='/api')


@gallery_bp.route('/gallery', methods=['GET'])
def list_images():
    ImageGallery = db_ImageGallery.find()

    ImageGallery_info = [{'id': ImageSet.get('id')} for ImageSet in ImageGallery]

    print(f"[后台] GET: 成功获取 {len(ImageGallery_info)} 个图集信息。")

    return jsonify(ImageGallery_info)


@gallery_bp.route('/set/<set_id>/thumbnail', methods=['GET'])
def get_thumbnail(set_id):
    result = db_ImageGallery.find_one({'id': set_id})
    if not result:
        return "Set not found", 404
    thumbnail_file_id = result.get('thumbnail_images')['file_id']
    image = db_fs.get(ObjectId(thumbnail_file_id))
    return send_file(
         BytesIO(image.read()),
         download_name=result.get('thumbnail_images')['file_name'],
         mimetype=image.content_type
    )
