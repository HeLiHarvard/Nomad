from app import db

class Trip(db.Model):
    '''
    Association Object
    '''

    __tablename__ = 'trip'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airport_from = db.Column(db.Integer, db.ForeignKey('airport.id'))
    airport_to = db.Column(db.Integer, db.ForeignKey('airport.id'))
    price = db.Column(db.Float)
    date = db.Column(db.Date)

class Airport(db.Model):

    __tablename__ = 'airport'

    id = db.Column(db.Integer, primary_key=True)
    iata = db.Column(db.String(8), index=True, unique=True)
    name = db.Column(db.String(120), index=True, unique=True)
    city = db.Column(db.String(120))
    region = db.Column(db.String(120))
    country = db.Column(db.String(120))

    flying_from = db.relationship('Trip', backref='end', primaryjoin=(id==Trip.airport_to))
    flying_to = db.relationship('Trip', backref='start', primaryjoin=(id==Trip.airport_from))

    def __repr__(self):
        return '<Airport: {0}; IATA: {1}>'.format(self.name, self.iata)




