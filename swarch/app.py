from flask import Flask
from config import DB_CONFIG
from models.grade import db
from controllers.grade_controller import grade_bp

def create_app():
    app = Flask(__name__)
    app.config.update(DB_CONFIG)
    db.init_app(app)
    app.register_blueprint(grade_bp)
    return app

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    # Usamos 0.0.0.0:8080 para que coincida con docker-compose
    app.run(host="0.0.0.0", port=8080, debug=True)
