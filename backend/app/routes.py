from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os


def init_routes(app: Flask):
    app.config['UPLOAD_FOLDER'] = 'uploads/'

    @app.route('/')
    def hello():
        return "Hello, BaKaBooru!"

    @app.route('/upload', methods=['POST'])
    def upload_image():
        if 'image' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({"message": "File uploaded successfully", "filename": filename}), 200

    if not os.path.exists('uploads'):
        os.makedirs('uploads')
