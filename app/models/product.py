from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.String(200), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.product_id
