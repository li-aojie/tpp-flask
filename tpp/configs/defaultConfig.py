# -*- coding:utf-8 -*-

# 秘钥
import os
KEY = os.environ.get("")

# 上传
# 说明：Linux系统时需要修改
plist = __file__.split("\\")
plist.pop()
plist.pop()
BASE_DIR = "\\".join(plist)
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static\media")


#日志
import logging
from logging.handlers import RotatingFileHandler
# 设置日志的记录级别
logging.basicConfig(level=logging.DEBUG)
# 日志文件
log_dir = os.path.join(BASE_DIR,"logs/t.log")
# 创建日志记录器，指明日志保存路径，每个日志文件的大小，保存日志的文件的上线
file_log_handler = RotatingFileHandler(log_dir, maxBytes=1024*1024*100,backupCount=10)
# 创建日志书写格式
formatter = logging.Formatter("%(levelname)s - %(filename)s - %(lineno)d - %(message)s")
# 为刚刚创建的日志记录器设置日志格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具添加记录器对象
logging.getLogger().addHandler(file_log_handler)


class DefaultConfig():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/jack"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg"