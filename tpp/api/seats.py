# -*- coding:utf-8 -*-
from flask import jsonify, request, session, make_response
from flask.ext.restful import Resource
from tpp.models import Seat, Hall, SeatSchedule

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("cinemaid", type=int)
parser.add_argument("hallid", type=int)
parser.add_argument("seattype", type=int)
parser.add_argument("x", type=int)
parser.add_argument("y", type=int)

class Seats(Resource):
    def get(self):
        hallid = request.args.get("hallid")
        hallScheduleid = request.args.get("hallScheduleid")

        seatschedules = SeatSchedule.query.filter_by(hallScheduleid=hallScheduleid)

        seatlist = Seat.query.filter_by(hallid=hallid)
        slist = []
        for seat in seatlist:
            obj = seat.toDict()
            for ss in seatschedules:
                if obj["id"] == ss.seatid:
                    obj["flag"] = 0
                    break;
            slist.append(obj)
        return {"code":200, "data":slist}
    def post(self):

        #假数据
        hlist = Hall.query.all()
        for hall in hlist:
            for x in range(3):
                for y in range(10):
                    seat = Seat(hall.cinemaid, hall.id, x, x, y)
                    seat.save()
        return "创建座椅成功"

    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass