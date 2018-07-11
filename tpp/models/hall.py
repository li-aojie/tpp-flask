# -*- coding:utf-8 -*-
'''
影厅表       halls
id
影院id
屏幕类型(2D、3D、4D)
音效类型(普通、环绕、杜比)
座位数量
状态(开放、关闭)
是否删除
'''
from tpp.exts import db, Model, TppFlag

class Hall(db.Model, Model):
    __tablename__ = "halls"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    cinemaid = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    # 2D、3D、4D
    screentype = db.Column(db.String(4))
    #普通、环绕、杜比
    soundtype = db.Column(db.String(8))
    seatnum = db.Column(db.Integer)
    # 1开放、0关闭
    flag = db.Column(db.Integer, default=TppFlag.OPEN)
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self, name, cinemaid, screentype, soundtype, seatnum):
        self.name = name
        self.cinemaid = cinemaid
        self.screentype = screentype
        self.soundtype = soundtype
        self.seatnum = seatnum