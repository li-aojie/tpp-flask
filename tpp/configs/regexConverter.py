# -*- coding:utf-8 -*-
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    def __init__(self, url, *args):
        super(RegexConverter, self).__init__(url)
        self.regex = args[0]