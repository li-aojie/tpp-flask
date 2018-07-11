# -*- coding:utf-8 -*-
from flask import jsonify, request
from flask.ext.restful import Resource
from tpp.models import HallSchedule, Hall, Movie

import random, datetime

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("cinemaid", type=int)
parser.add_argument("hallid", type=int)
parser.add_argument("movieid", type=int)
parser.add_argument("pricetype", type=int)
parser.add_argument("price0", type=float)
parser.add_argument("price1", type=float)
parser.add_argument("price2", type=float)
parser.add_argument("showdate", type=str)
parser.add_argument("starttime", type=str)
parser.add_argument("endtime", type=str)

class HallSchedules(Resource):
    def get(self):
        cinemaid = request.args.get("cinemaid")
        showdate = request.args.get("showdate")
        movieid = request.args.get("movieid")

        hslist = HallSchedule.query.filter_by(cinemaid=cinemaid)

        if (not showdate) and (not movieid):
            datelist = []
            for hs in hslist:
                datelist.append(hs.showdate.strftime("%Y-%m-%d"))
            datelist = list(set(datelist))
            return jsonify({"code":200, "datelist":datelist})

        elif not movieid:
            d = datetime.datetime.strptime(showdate,"%Y-%m-%d")
            hslist = hslist.filter_by(showdate=d)
            movielist = []
            for hs in hslist:
                movie = Movie.query.get(hs.movieid)
                movielist.append(movie.chname)
            movielist = list(set(movielist))
            return jsonify({"code": 200, "movielist": movielist})
        else:
            d = datetime.datetime.strptime(showdate, "%Y-%m-%d")
            hslist = hslist.filter_by(showdate=d)
            hslist = hslist.filter_by(movieid=movieid)
            hsslist = []
            for hs in hslist:
                hsslist.append(hs.toDict())
            return jsonify({"code": 200, "date": hsslist})

    def post(self):
        # args = parser.parse_args()
        # hallSchedule = HallSchedule(args["cinemaid"],args["hallid"],args["movieid"],args["pricetype"],args["price0"],args["price1"],args["price2"],args["showdate"],args["starttime"],args["endtime"])
        # msg = hallSchedule.save()
        # if msg:
        #     return jsonify({"code": 400, "msg": msg})
        # else:
        #     return jsonify({"code":201, "data":hallSchedule.toDict()})


        # 假数据
        slist = ["08:00:00","10:00:00","12:00:00","14:00:00","16:00:00"]
        nlist = ["09:30:00", "11:30:00", "13:30:00", "15:30:00", "17:30:00"]
        #正在热映的电影
        mlist = Movie.query.filter_by(flag=1)
        #所有影厅
        hlist = Hall.query.all()
        for hall in hlist:
            for index in range(5):
                movie = random.choice(list(mlist))
                hallSchedule = HallSchedule(hall.cinemaid, hall.id, movie.id, 0, 5, 4, 3, "2018-03-28", slist[index], nlist[index])
                hallSchedule.save()
        return "增加影厅排期假数据成功"
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass