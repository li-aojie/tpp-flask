# -*- coding:utf-8 -*-
from flask import Flask
from tpp.configs import DevelopmentConfig,TestingConfig,ProductConfig,RegexConverter
from tpp.exts import db, api
from tpp.api import urls

def create_app():
    # 创建app对象
    app = Flask("tpp")
    app.config.from_object(DevelopmentConfig)
    app.url_map.converters["regex"] = RegexConverter

    db.init_app(app)
    api.init_app(app)
    app.register_blueprint(urls)

    return app