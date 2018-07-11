# -*- coding:utf-8 -*-
from tpp.exts import db, Model

class Seat(db.Model, Model):
    __tablename__ = "seats"
    id = db.Column(db.Integer, primary_key=True)
    cinemaid = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallid = db.Column(db.Integer, db.ForeignKey("halls.id"))
    # 座位类型(0板凳、1沙发、2床)
    seattype = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    # isShow = db.Column(db.Boolean)
    # 1正常 0损坏
    flag = db.Column(db.Integer, default=1)

    def __init__(self,cinemaid,hallid,seattype,x,y):
        self.cinemaid = cinemaid
        self.hallid = hallid
        self.seattype = seattype
        self.x = x
        self.y = y
