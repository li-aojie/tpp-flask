# -*- coding:utf-8 -*-
from flask import jsonify, request
from flask.ext.restful import Resource
from tpp.models import Hall, Cinema

import random

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("cinemaid", type=int)
parser.add_argument("screentype", type=str)
parser.add_argument("soundtype", type=str)
parser.add_argument("seatnum", type=int)
parser.add_argument("flag", type=int)

class Halls(Resource):
    def get(self):
       pass
    def post(self):
        # 假数据
        names = ["桃花源","乌托邦","梅花岛","枫林院"]
        screens = ["2D","3D","4d"]
        sounds = ["普通","环绕","杜比"]
        # 给每个影院创建4个影厅
        clist = Cinema.query.all()
        for cinema in clist:
            for index in range(4):
                print("****************************")
                print(cinema.id, names[index], random.choice(screens), random.choice(sounds), 30)
                hall = Hall(names[index], cinema.id, random.choice(screens), random.choice(sounds), 30)
                hall.save()
        return "影厅创建成功"
    def put(self):
        pass
    def patch(self):
        args = parser.parse_args()
        halls = Hall.query.get(args["id"])
        halls.screentype = "1D"
        halls.isDelete = True
        halls.save()
        return "修改成功"
    def delete(self):
        args = parser.parse_args()
        hallsid = Hall.query.get(args["id"])
        hallsid.delete()
        return "影厅删除成功！"