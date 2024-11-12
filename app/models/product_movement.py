from app import db
from datetime import datetime
from .product import Product
from .location import Location

class ProductMovement(db.Model):
    __tablename__ = 'productmovements'
    movement_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    qty = db.Column(db.Integer)
    from_location = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    to_location = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    movement_time = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship('Product', foreign_keys=product_id)
    fromLoc = db.relationship('Location', foreign_keys=from_location)
    toLoc = db.relationship('Location', foreign_keys=to_location)

    def __repr__(self):
        return '<ProductMovement %r>' % self.movement_id
