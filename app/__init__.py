from flask import Flask
from flask_migrate import Migrate
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# csrf = CSRFProtect(app)
app.config.from_object(Config)



# app.config['WTF_CSRF_ENABLED'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import views