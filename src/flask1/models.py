
"""Data models."""
from . import db

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))


    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

    def __repr__(self):
        return "<User {}>".format(self.username)

class ohlc_test(db.Model):
    id = db.Column('ohlc_id', db.Integer, primary_key=True)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    dt = db.Column(db.DateTime)
    symbol = db.Column(db.String(20))
    volume = db.Column(db.Float)

    def __init__(self, symbol, dt, open, high, low, close, volume):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.dt = dt
        self.symbol = symbol
        self.volume = volume

    def __repr__(self):
        return "<User {}>".format(self.username)