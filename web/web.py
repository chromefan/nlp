# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 下午9:00
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : web.py

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        greeting = self.get_argument('greeting', 'my friend')
        self.write('Hello ' + greeting + ', This is Tornado!')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
