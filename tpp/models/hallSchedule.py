# -*- coding:utf-8 -*-
from tpp.exts import db, Model

class HallSchedule(db.Model, Model):
    __tablename__ = "hallschedules"
    id = db.Column(db.Integer, primary_key=True)
    cinemaid = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallid = db.Column(db.Integer, db.ForeignKey("halls.id"))
    movieid = db.Column(db.Integer, db.ForeignKey("movies.id"))
    # 0原价、1售价、2特惠价
    pricetype = db.Column(db.Integer)
    price0 = db.Column(db.Float)
    price1 = db.Column(db.Float)
    price2 = db.Column(db.Float)

    showdate = db.Column(db.Date)
    starttime = db.Column(db.Time)
    endtime = db.Column(db.Time)

    # 0未放映、1正在放映、2结束放映
    flag = db.Column(db.Integer, default=0)
    isDelete = db.Column(db.Boolean, default=False)

    def __init__(self,cinemaid,hallid,movieid,pricetype,price0,price1,price2,showdate,starttime,endtime):
        self.cinemaid=cinemaid
        self.hallid =hallid
        self.movieid =movieid
        self.pricetype =pricetype
        self.price0 =price0
        self.price1 =price1
        self.price2 =price2
        self.showdate =showdate
        self.starttime =starttime
        self.endtime =endtime

