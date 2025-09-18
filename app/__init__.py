from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app(config_class: type = Config) -> Flask:
    """
    Flask application factory.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    

    # import models to register them with SQLAlchemy metadata
    from .models import (hotel, habitacion, calendario_habitacion, oferta,
                         cliente, reserva, pago, politica_cancelacion, comentario)  # noqa

    # Register blueprints or routes (example)
    from.views import bp
    app.register_blueprint(bp) 

    return app
