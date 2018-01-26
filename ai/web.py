# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 下午9:00
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : web.py

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import pandas as pd
from tornado.options import define, options

from nlp.NBclassifier import NBclassifier
from words.Words import Words

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        text = self.get_argument('text', '')
        word = Words()
        word_str = word.cut_words(text)
        self.write(word_str)
        clf_path = "./datasets/trainModel/clf.m"
        vec_path = "./datasets/trainModel/vec.m"
        # 创建NB分类器
        nbclassifier = NBclassifier(clf_path, vec_path)
        data_list = [word_str]
        predictList = nbclassifier.predict(data_list)
        predictList = list(predictList)
        self.write(json.dumps(predictList, ensure_ascii=False))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/nlp", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
