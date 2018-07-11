# -*- coding:utf-8 -*-
from flask import jsonify, request, session, make_response
from flask.ext.restful import Resource
from tpp.models import Order, SeatSchedule, Seat

import random,time

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("movieid", type=int)
parser.add_argument("cinemaid", type=int)
parser.add_argument("hallid", type=int)
parser.add_argument("hallScheduleid", type=int)
parser.add_argument("seatidlist", type=str)
parser.add_argument("pnum", type=int)

class Orders(Resource):
    def get(self):
        pass
    def post(self):
        args = parser.parse_args()
        userid = "1"
        pstr = "123456"
        price = 15
        order = Order(userid, args["movieid"],args["cinemaid"],args["hallid"],args["hallScheduleid"],args["pnum"],pstr, args["seatidlist"],price)
        order.save()

        #0:0,0:1
        seatlist = args["seatidlist"].split(",")
        for seatxy in seatlist:
            x = seatxy.split(":")[0]
            y = seatxy.split(":")[1]
            seat = Seat.query.filter_by(hallid=args["hallid"]).filter_by(x=x).filter_by(y=y)[0]
            seatSchedules = SeatSchedule(args["cinemaid"],args["hallid"],seat.id,args["hallScheduleid"],order.id)
            seatSchedules.save()
        return "创建订单成功"
    def put(self):
        pass
    def patch(self):
        args = parser.parse_args()
        order = Order.query.get(args["id"])
        order.isDelete = False
        msg = order.save()
        print("*****************************")
        print(msg)
        return "修改订单成功"
    def delete(self):
        pass