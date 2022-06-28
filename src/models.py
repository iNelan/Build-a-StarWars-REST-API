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
    password = db.Column(db.String(80), unique=False, nullable=False)
    favourites = db.relationship('Favourites', backref = 'User')


    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    __tablename__ = 'characters'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(20), nullable = False)
    mass = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    addresses = db.relationship('Favourites', backref='characters', lazy=True)


    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "mass": self.mass,
            "height": self.height,
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    diameter = db.relationship('Favourites', backref='planets', lazy=True)


    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lenght = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    cost = db.relationship('Favourites', backref='vehicles', lazy=True)


    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lenght": self.lenght,
            "passengers": self.passengers,
            # do not serialize the password, its a security breach
        }


class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'),
        nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'),
        nullable=False)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'),
        nullable=False)
    

    def __repr__(self):
        return '<Favourites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id,
            "planets_id": self.planets_id,
            "vehicles_id": self.vehicles_id,
            # do not serialize the password, its a security breach
        }