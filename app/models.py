from app import db

class Airport(db.Model):
    name = db.Column(db.String(120), index=True, unique=True)
    iata = db.Column(db.String(8), index=True, primary_key=True)

    def __repr__(self):
        return '<Airport: {0}>\n<IATA code: {1}>'.format(self.name, self.iata)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String(8), db.ForeignKey('airport.iata'))
    end = db.Column(db.String(8), db.ForeignKey('airport.iata'))
    price = db.Column(db.Decimal(8,4))

    def __repr__(self):
        return '<Price for trip from {0} to {1}: ${2}>'.format(self.start, self.end, self.price)
