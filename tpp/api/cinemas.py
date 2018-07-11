# -*- coding:utf-8 -*-
from flask import jsonify, request
from flask.ext.restful import Resource
from tpp.models import Cinema

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("name", type=str)
parser.add_argument("city", type=str)
parser.add_argument("district", type=str)
parser.add_argument("address", type=str)
parser.add_argument("phone", type=str)
parser.add_argument("score", type=float)
parser.add_argument("hallnum", type=int)
parser.add_argument("servicecharge", type=float)
parser.add_argument("astrict", type=int)
parser.add_argument("flag", type=int)

class Cinemas(Resource):
    def get(self):
        cityid = request.args.get("cityid")
        district = request.args.get("district")
        sortby = request.args.get("sortby")
        order = request.args.get("order")
        offset = request.args.get("offset")
        limit = request.args.get("limit")

        clist = Cinema.query.filter_by(city=cityid)
        if district != "全部区域":
            clist = clist.filter_by(district=district)

        clist = clist.order_by(-Cinema.score).offset(offset).limit(limit)

        datelist = []
        for cinema in clist:
            datelist.append(cinema.toDict())

        return {"code":200, "date":datelist}

    def post(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass