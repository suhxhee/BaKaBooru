from flask import Blueprint, request, jsonify
from backend.db import db_fs, db_ImageGallery

delete_bp = Blueprint('delete', __name__, url_prefix='/api')


@delete_bp.route('/gallery/clear', methods=['DELETE'])
def clear_gallery():
    count = db_ImageGallery.count_documents({})
    file_ids = db_fs.find().distinct('_id')  # 获取所有文件的 ID
    for file_id in file_ids:
        db_fs.delete(file_id)  # 删除每个文件
    db_ImageGallery.delete_many({})
    print(f"已清空所有图集({count}个)。")
    return jsonify({'message': '删除成功'}), 200
