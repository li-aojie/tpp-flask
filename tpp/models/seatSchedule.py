from tpp.exts import db, Model

class SeatSchedule(db.Model, Model):
    __tablename__ = "seatschedules"
    id = db.Column(db.Integer, primary_key=True)
    cinemaid = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallid = db.Column(db.Integer, db.ForeignKey("halls.id"))
    seatid = db.Column(db.Integer, db.ForeignKey("seats.id"))
    hallScheduleid = db.Column(db.Integer, db.ForeignKey("hallschedules.id"))
    orderid = db.Column(db.Integer, db.ForeignKey("orders.id"))
    def __init__(self,cinemaid,hallid,seatid,hallScheduleid,orderid):
        self.cinemaid = cinemaid
        self.hallid = hallid
        self.seatid = seatid
        self.hallScheduleid = hallScheduleid
        self.orderid = orderid
