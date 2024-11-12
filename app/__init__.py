from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
    db.init_app(app)

    from .controllers.main_controller import main_bp
    from .controllers.product_controller import product_bp
    from .controllers.location_controller import location_bp
    from .controllers.movement_controller import movement_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(location_bp, url_prefix='/locations')
    app.register_blueprint(movement_bp, url_prefix='/movements')

    return app
