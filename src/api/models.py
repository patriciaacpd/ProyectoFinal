from flask_sqlalchemy import SQLAlchemy
import enum


db = SQLAlchemy()

class Role(enum.Enum):
    admin = "admin"
    user = "user"

class RoomStatus(enum.Enum):
    avaible= "avaible"
    busy= "busy"
    maintenance= "maintenance"
    not_avaible= "not_Avaible"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_name= db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    role= db.Column(db.Enum(Role), nullable=False, default="user")

class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(80), unique=True, nullable=False)
    room_type = db.Column(db.String(120), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    status= db.Column(db.Enum(RoomStatus), unique= False, nullable=False)
    user= db.relationship('User',backref='rooms')
    user_id= db.Column(db.Integer,db.ForeignKey('user.id'))
def serialize(self):
    return {
            "id":self.id,
            "number": self.number,
            "room_type": self.room_type,
            "status": self.status,
        }


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    lastname= db.Column(db.String(120))
    document = db.Column(db.String(80), unique=True, nullable=False)
    occupation= db.Column(db.String(80))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    email = db.Column(db.String(80))
    def serialize(self):
        return {
            "name": self.name,
            "document": self.document,
            "lastname": self.lastname,
            "occupation": self.occupation,
            "email": self.email
        }

class checkin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_in= db.Column(db.DateTime, nullable=False)
    time_out= db.Column(db.DateTime, nullable=False)
    observations= db.Column(db.String(200))
    Rooms= db.relationship(Rooms)
    Rooms_id= db.Column(db.Integer,db.ForeignKey('rooms.id'), nullable=True)
    customer= db.relationship(Customer)
    customer_id= db.Column(db.Integer,db.ForeignKey('customer.id'), nullable=True)



    def __repr__(self):
        return f'<User {self.email}>'

