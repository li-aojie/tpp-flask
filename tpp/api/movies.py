# -*- coding:utf-8 -*-
from flask import jsonify, request
from flask.ext.restful import Resource
from tpp.models import Movie

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("chname", type=str)
parser.add_argument("enname", type=str)
parser.add_argument("director", type=str)
parser.add_argument("leadingRole", type=str)
parser.add_argument("type", type=str)
parser.add_argument("country", type=str)
parser.add_argument("language", type=str)
parser.add_argument("duration", type=int)
parser.add_argument("screeningmodel", type=str)
parser.add_argument("openday", type=str)
parser.add_argument("backgroundpicture", type=str)
parser.add_argument("flag", type=int)

class Movies(Resource):
    def get(self):
        flag = request.args.get("flag")
        sortby = request.args.get("sortby")
        order = request.args.get("order")
        limit = request.args.get("limit")

        mlist = Movie.query.filter_by(flag=flag)
        if sortby:
            if order == "desc":
                sortby = "-" + sortby
            mlist = mlist.order_by(sortby)
        if limit:
            mlist = mlist.limit(int(limit))

        rlist = []
        for movie in mlist:
            rlist.append(movie.toDict())

        return jsonify({"code":200, "data":rlist})

    def post(self):
        args = parser.parse_args()
        movie = Movie(args["id"],args["chname"],args["enname"],args["director"],args["leadingRole"],args["type"],args["country"],args["language"],args["duration"],args["screeningmodel"],args["openday"],args["backgroundpicture"],args["flag"])
        msg = movie.save()
        if msg:
            return jsonify({"code": 400, "msg": msg})
        else:
            return jsonify({"code":201,"data":movie.toDict()})
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        args = parser.parse_args()
        idlist = Movie.query.get(args["id"])
        idlist.delete()
        return "电影删除成功！"