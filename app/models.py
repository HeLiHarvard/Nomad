from app import db

trips = db.Table('trips',
    db.Column('start_id', db.Integer, db.ForeignKey('airport.id')),
    db.Column('end_id', db.Integer, db.ForeignKey('airport.id'))
)

class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iata = db.Column(db.String(8), index=True, unique=True)
    name = db.Column(db.String(120), index=True, unique=True)
    location = db.Column(db.String(120))

    destinations = db.relationship('Airport',
                          secondary=trips,
                          primaryjoin=(trips.c.start_id == id),
                          secondaryjoin=(trips.c.end_id == id),
                          backref=db.backref('starts', lazy='dynamic'),
                          lazy='dynamic')

    def __repr__(self):
        return '<Airport: {0}; IATA: {1}>'.format(self.name, self.iata)

