from bson import ObjectId
from flask import Blueprint, request, jsonify
from backend.db import db_fs, db_ImageGallery, reset_sequence

delete_bp = Blueprint('delete', __name__, url_prefix='/api')


@delete_bp.route('/gallery/clear', methods=['DELETE'])
def clear_gallery():
    count = db_ImageGallery.count_documents({})
    file_ids = db_fs.find().distinct('_id')  # 获取所有文件的 ID
    for file_id in file_ids:
        db_fs.delete(file_id)  # 删除每个文件
    db_ImageGallery.delete_many({})
    reset_sequence('set_id')  # 重置set_id计数器
    print(f"已清空所有图集({count}个)。")
    return jsonify({'message': f"已清空所有图集({count}个)。"}), 200


@delete_bp.route('/set/<set_id>/delete', methods=['DELETE'])
def delete_set(set_id):
    set_info = db_ImageGallery.find_one({'id': set_id})
    if not set_info:
        return "找不到该图集。", 404
    # 删除缩略图
    db_fs.delete(ObjectId(set_info.get('thumbnail_images')['file_id']))
    # 删除源文件
    original_images = set_info.get('original_images')
    for image in original_images:
        db_fs.delete(ObjectId(original_images[image]['file_id']))
    # 删除图集信息
    db_ImageGallery.delete_one({'_id': ObjectId(set_info.get('_id'))})

    print(f"已删除图集(set_id:{set_id})。")
    return jsonify({'message': f"已删除图集(set_id:{set_id})。"}), 200
