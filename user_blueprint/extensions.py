from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_extensions(app):
    """
    初始化所有Flask扩展
    """
    db.init_app(app)
    migrate.init_app(app, db)