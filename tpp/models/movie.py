# -*- coding:utf-8 -*-
from tpp.exts import db, Model, TppFlag

class Movie(db.Model, Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    chname = db.Column(db.String(64))
    enname = db.Column(db.String(64))
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(256))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    screeningmodel = db.Column(db.String(8))
    openday = db.Column(db.Date)
    backgroundpicture = db.Column(db.String(256))
    # 1即将上映 2正在热映
    flag = db.Column(db.Integer)
    isDelete = db.Column(db.Boolean, default=False)

    def __init__(self, id, chName, enName, director, leadingRole, type, country, language, duration, screeningmodel, openday, backgroundpicture, flag):
        self.id = id
        self.chname = chName
        self.enname = enName
        self.director = director
        self.leadingRole = leadingRole
        self.type = type
        self.country = country
        self.language = language
        self.duration = duration
        self.screeningmodel = screeningmodel
        self.openday = openday
        self.backgroundpicture = backgroundpicture
        self.flag = flag