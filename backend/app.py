from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 注册蓝图
from api.upload import upload_bp
from api.images import images_bp

app.register_blueprint(upload_bp)
app.register_blueprint(images_bp)

if __name__ == '__main__':
    app.run(debug=True)
