# -*- coding:utf-8 -*-
from tpp.exts import db, Model

class Cinema(db.Model, Model):
    __tablename__ = "cinemas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    city = db.Column(db.String(32))
    district = db.Column(db.String(32))
    address = db.Column(db.String(128))
    phone = db.Column(db.String(16))
    score = db.Column(db.Float)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Float)
    astrict = db.Column(db.Integer)
    # 1营业、0休息
    flag = db.Column(db.Integer, default=1)
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self, name, city, district, address, phone, score, hallnum, servicecharge, astrict, flag):
        self.name = name
        self.city = city
        self.district = district
        self.address = address
        self.phone = phone
        self.score = score
        self.hallnum = hallnum
        self.servicecharge = servicecharge
        self.astrict = astrict
        self.flag = flag