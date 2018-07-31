from sqlalchemy import func
from app.create_app import db
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField
)


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    village = db.Column(db.String(200))
    district = db.Column(db.String(200))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    address = db.Column(db.Text)
    trash = db.Column(db.Boolean, default=0, nullable=False)
    create_at = db.Column(db.DateTime, default=func.current_timestamp())
    update_at = db.Column(db.DateTime, onupdate=func.now())
    delete_at = db.Column(db.DateTime)

    def location_form(self, form):
        self.village = form.village.data
        self.district = form.district.data
        self.address = form.address_loc.data
        self.lat = form.lat.data
        self.lng = form.lng.data


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))
    alt = db.Column(db.String(200))
    trash = db.Column(db.Boolean, default=0, nullable=False)
    create_at = db.Column(db.DateTime, default=func.current_timestamp())
    update_at = db.Column(db.DateTime, onupdate=func.now())
    delete_at = db.Column(db.DateTime)


class Feature(db.Model):
    __tablename__ = 'feature'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    count_feature = db.Column(db.Integer)
    desc = db.Column(db.Text)
    trash = db.Column(db.Boolean, default=0, nullable=False)
    photos = db.relationship(
        'Photo', 
        secondary='photo_feature_wisata', 
        backref=db.backref(
            'feature', 
            lazy='dynamic'
        )
    )
    create_at = db.Column(db.DateTime, default=func.current_timestamp())
    update_at = db.Column(db.DateTime, onupdate=func.now())
    delete_at = db.Column(db.DateTime)


class Administrator(db.Model):
    __tablename__ = 'administrator'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    desc = db.Column(db.Text)
    contact = db.Column(db.String(45))
    address = db.Column(db.Text)
    trash = db.Column(db.Boolean, default=0, nullable=False)
    create_at = db.Column(db.DateTime, default=func.current_timestamp())
    update_at = db.Column(db.DateTime, onupdate=func.now())
    delete_at = db.Column(db.DateTime)

    def admin_form(self, form):
        self.name = form.admin_name.data
        self.first_name = form.first_name.data
        self.last_name = form.last_name.data
        self.contact = form.contact.data
        self.address = form.address_admin.data


class Wisata(db.Model):
    __tablename__ = 'wisata'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    desc = db.Column(db.Text)
    features = db.relationship(
        'Feature', 
        secondary='features_wisata', 
        backref=db.backref(
            'wisata', 
            lazy='dynamic'
        )
    )
    location_id = db.Column(
        db.Integer, 
        db.ForeignKey('location.id', 
        ondelete='CASCADE')
    )
    location = db.relationship(
        'Location', 
        foreign_keys=location_id, 
        backref=db.backref('location_wisata')
    )
    admin_id = db.Column(
        db.Integer, 
        db.ForeignKey('administrator.id', 
        ondelete='CASCADE')
    )
    admin = db.relationship(
        'Administrator', 
        foreign_keys=admin_id, 
        backref=db.backref('administrator_wisata')
    )
    trash = db.Column(db.Boolean, default=0, nullable=False)
    photos = db.relationship(
        'Photo', 
        secondary='photo_wisata', 
        backref=db.backref(
            'wisata', 
            lazy='dynamic'
        )
    )
    create_at = db.Column(db.DateTime, default=func.current_timestamp())
    update_at = db.Column(db.DateTime, onupdate=func.now())
    delete_at = db.Column(db.DateTime)

    @staticmethod
    def get_all_data(search="", page = 1, perpage = 15):
        return Wisata.query.filter(
            Wisata.name.like('%{}%'.format(search))
        ).paginate(page, perpage, False)
    
    @staticmethod
    def get_by_id(wisata_id):
        return Wisata.query.get(wisata_id)

    def wisata_form(self, form):
        self.name = form.name.data
        self.desc = form.desc.data

    def save(self):
        db.session.add(self)
        db.session.commit()


class PhotoWisata(db.Model):
    __tablename__ = 'photo_wisata'
    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id', ondelete='CASCADE'))
    wisata_id = db.Column(db.Integer, db.ForeignKey('wisata.id', ondelete='CASCADE'))


class PhotoFeatureWisata(db.Model):
    __tablename__ = 'photo_feature_wisata'
    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id', ondelete='CASCADE'))
    feature_id = db.Column(db.Integer, db.ForeignKey('feature.id', ondelete='CASCADE'))


class FeaturesWisata(db.Model):
    __tablename__ = 'features_wisata'
    id = db.Column(db.Integer, primary_key=True)
    wisata_id = db.Column(db.Integer, db.ForeignKey('wisata.id', ondelete='CASCADE'))
    feature_id = db.Column(db.Integer, db.ForeignKey('feature.id', ondelete='CASCADE'))
