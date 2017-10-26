from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType

db = SQLAlchemy()

class Track(db.Model):
    id = db.Column(UUIDType(binary=False), primary_key=True)
    name = db.Column(db.String(255), nullable=False)