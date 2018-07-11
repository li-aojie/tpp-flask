# -*- coding:utf-8 -*-
from flask import jsonify, request, session, make_response
from flask.ext.restful import Resource
from tpp.models import User

import random,time

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("account", type=str)
parser.add_argument("passwd", type=str)
parser.add_argument("name", type=str)

class Users(Resource):
    #查看用户信息
    def get(self):
        pass
    #注册
    def post(self):
        args = parser.parse_args()
        account = args["account"]
        user = User.query.get(account)
        if user:
            return {"code":400,"msg":"账号被占用"}
        passwd = args["passwd"]
        name = args["name"]
        token = str(time.time())
        user = User(account, passwd, name, token)
        user.save()
        object = {}
        object["name"] = user.name
        object["account"] = user.account
        data = {"code":201,"date":object}
        #状态保持
        session["username"] = name
        response = make_response(jsonify(data))
        response.set_cookie("name","username")
        response.set_cookie("token", token)

        return response
    #修改用户信息
    def put(self):
        pass
    def patch(self):
        pass
    #删除用户
    def delete(self):
        pass