# -*- coding:utf-8 -*-
from tpp.exts import db, Model

class User(db.Model, Model):
    __tablename__ = "users"
    account = db.Column(db.String(16), primary_key=True)
    passwd = db.Column(db.String(16))
    name = db.Column(db.String(16))
    token = db.Column(db.String(64))
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self,account,passwd,name,token):
        self.account = account
        self.passwd = passwd
        self.name = name
        self.token = token