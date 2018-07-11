# -*- coding:utf-8 -*-
from flask import jsonify, request
from flask.ext.restful import Resource
from tpp.models import User

# 表单参数
from flask.ext.restful import reqparse
parser = reqparse.RequestParser()
parser.add_argument("accout", type=str)
parser.add_argument("passwd", type=str)

class Login(Resource):
    #登陆
    def post(self):
        pass