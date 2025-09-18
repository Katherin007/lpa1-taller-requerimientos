from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Singletons for app extensions
db = SQLAlchemy()
migrate = Migrate()
