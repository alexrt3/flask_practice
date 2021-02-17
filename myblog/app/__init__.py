from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from config import Config
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    login_manager.init_app(app)
    
    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # Needs app context
    with app.app_context():
        from app import views

    return app