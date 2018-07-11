# -*- coding:utf-8 -*-
from tpp.exts import db, Model

from sqlalchemy import text
from sqlalchemy.sql import func
'''
id
用户id
电影id
影院id
影厅id
影厅排期id

座位id列表 1,2

票数
取票码

创建时间
修改时间
支付时间
取票时间
退款时间
状态(未支付、已支付未取票、已支付已取票)
是否删除
'''

class Order(db.Model, Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(16), db.ForeignKey("users.account"))
    movieid = db.Column(db.Integer, db.ForeignKey("movies.id"))
    cinemaid = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallid = db.Column(db.Integer, db.ForeignKey("halls.id"))
    hallScheduleid = db.Column(db.Integer, db.ForeignKey("hallschedules.id"))

    seatidlist = db.Column(db.String(16))

    pnum = db.Column(db.Integer)
    price = db.Column(db.Float)
    pstr = db.Column(db.String(16))

    createTime = db.Column(db.TIMESTAMP(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    changeTime = db.Column(db.Time, onupdate=func.now())
    payTime = db.Column(db.Time)
    getTime = db.Column(db.Time)
    backTime = db.Column(db.Time)
    # 0未支付、1已支付未取票、2已支付已取票
    flag = db.Column(db.Integer, default=0)
    isDelete = db.Column(db.Boolean, default=False)

    def __init__(self,userid,movieid,cinemaid,hallid,hallScheduleid,pnum,pstr,seatidlist,price):
        self.userid = userid
        self.movieid = movieid
        self.cinemaid = cinemaid
        self.hallid = hallid
        self.hallScheduleid = hallScheduleid
        self.seatidlist = seatidlist
        self.pstr = pstr
        self.pnum = pnum
        self.price = price