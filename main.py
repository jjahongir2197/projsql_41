from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///json.db'
db = SQLAlchemy(app)

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON)

with app.app_context():
    db.create_all()

    s = Settings(data={"theme": "dark", "language": "uz"})
    db.session.add(s)
    db.session.commit()
