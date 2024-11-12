from app import db
from datetime import datetime

class Location(db.Model):
    __tablename__ = 'locations'
    location_id = db.Column(db.String(200), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Location %r>' % self.location_id
