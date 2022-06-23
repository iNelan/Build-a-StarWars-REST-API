from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.db.Column(db.Integer, primary_key=True)
#     email = db.db.Column(db.String(120), unique=True, nullable=False)
#     password = db.db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }


db = SQLAlchemy()




class  User(db.Model):
    __tablename__ = 'user'
    # Here we define db.Columns for the table person
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    addresses = db.relationship('Favourites', backref='user', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    addresses = relationship('Favourites', backref='characters', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    diameter = db.relationship('Favourites', backref='planets', lazy=True)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lenght = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    cost = db.relationship('Favourites', backref='vehicles', lazy=True)


class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = db.Column(Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'),
        nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'),
        nullable=False)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'),
        nullable=False)