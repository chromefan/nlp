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
from tornado.options import define, options

from nlp.NBclassifier import NBclassifier
from words.Words import Words

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        text = self.get_argument('text', '')
        cut_word = self.get_argument('cut_word', 0)
        word = Words()
        word_str = word.cut_words(text)

        if int(cut_word) == 1:
            result = {'msg': 'ok', 'data': word_str}
            result = json.dumps(result, ensure_ascii=False)
            self.write(result)
            return

        clf_path = "./datasets/trainModel/clf.m"
        vec_path = "./datasets/trainModel/vec.m"
        # 创建NB分类器
        nbclassifier = NBclassifier(clf_path, vec_path)
        data_list = [word_str]
        predictList = nbclassifier.predict(data_list)
        predictList = list(predictList)
        predict_class = "".join(predictList)
        result = {'msg': 'ok', 'data': predict_class}
        result = json.dumps(result, ensure_ascii=False)
        self.write(result)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/nlp", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
