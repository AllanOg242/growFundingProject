from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
'''login_manager = LoginManager()
admin_login_manager = LoginManager()
admin_login_manager.login_view = 'admin.adminlogin'''


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    db.init_app(app)
    #login_manager.init_app(app)
    #admin_login_manager.init_app(app)

    from app.hopital import hopital as hopital_blueprint
    from app.admin import admin as admin_blueprint
    app.register_blueprint(hopital_blueprint)
    app.register_blueprint(admin_blueprint)

    return app
