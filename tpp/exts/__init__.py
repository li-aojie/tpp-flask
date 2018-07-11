# -*- coding:utf-8 -*-
from tpp.exts.extends import db, api


import datetime
class Model():
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    @classmethod
    def save_all(cls, dataList):
        try:
            db.session.add_all(dataList)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e)
    def toDict(self):
        keys = vars(self).keys()
        obj = {}
        for key in keys:
            if not key.startswith("_"):
                if isinstance(getattr(self, key), datetime.date) or isinstance(getattr(self, key), datetime.time) or isinstance(getattr(self, key), datetime.datetime):
                    obj[key] = getattr(self,key).strftime("%Y-%m-%d")
                else:
                    obj[key] = getattr(self,key)
        return obj


# 枚举
class TppFlag():
    HOT_SHOWING = 2
    COMMING_SOON = 1

    OPEN = 1
    CLOSE = 0

