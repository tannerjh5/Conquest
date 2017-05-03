from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'hi'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
db = SQLAlchemy(app)


from app import views
#from app import models, views
#db.create_all()
#db.drop_all()
#models.Post.__table__.drop(db.engine)