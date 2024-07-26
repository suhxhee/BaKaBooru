from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 注册蓝图
from api.upload import upload_bp
from api.gallery import gallery_bp

app.register_blueprint(upload_bp)
app.register_blueprint(gallery_bp)

if __name__ == '__main__':
    app.run(debug=True)
