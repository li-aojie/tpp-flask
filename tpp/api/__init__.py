# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, current_app, request, make_response, redirect, url_for, abort, session, g, jsonify
from tpp.models import *
import logging
from tpp.exts import api

urls = Blueprint("tpp", 'urls', template_folder="templates")

@urls.route('/')
def index():
    url = url_for("tpp.staticFile", _external=True, filename="index.html")
    return redirect(url)
# 访问静态文件
@urls.route("/<regex('.*'):filename>")
def staticFile(filename):
    if not filename:
        filename = "html/index.html"
    if filename != "favicon.ico":
        filename = "html/" + filename
    #返回静态文件
    response = make_response(current_app.send_static_file(filename))
    return response
# 错误视图
@urls.app_errorhandler(404)
def handler404(exception):
    return render_template("404.html"), 404


from tpp.api.movies import Movies
api.add_resource(Movies,"/movies/")

from tpp.api.cinemas import Cinemas
api.add_resource(Cinemas,"/cinemas/")

from tpp.api.halls import Halls
api.add_resource(Halls,"/halls/")

from tpp.api.hallSchedules import HallSchedules
api.add_resource(HallSchedules,"/hallSchedules/")

from tpp.api.users import Users
api.add_resource(Users,"/users/")

from tpp.api.seats import Seats
api.add_resource(Seats,"/seats/")

from tpp.api.orders import Orders
api.add_resource(Orders,"/orders/")