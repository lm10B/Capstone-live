from flask import Flask

from config import Config
from extensions import db

from routes.main import main_bp
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.donation import donation_bp


def create_app():

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Connect database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(donation_bp)

    from models import User, Member, Donor, Donation
    with app.app_context():
        db.create_all()

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=False)