from app import db

class Base(db.Model):    
    __abstract__ = True
    id            = db.Column(db.Integer,  primary_key=True)
    data_created  = db.Column(db.DataTime, default=db.func.current_timestamp())
    data_modified = db.Column(db.DataTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp)


class User(Base):
    __tablename__ = 'auth_user'
    name     = db.Column(db.String(128),  nullable=False)
    email    = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    role     = db.Column(db.SmallInteger, nullable=False)
    status   = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, name, email, password):
        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
