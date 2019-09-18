from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "ubersecretkeythatIwillchangelater"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contents.db'
db = SQLAlchemy(app)
