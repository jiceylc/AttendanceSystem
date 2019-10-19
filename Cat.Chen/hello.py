import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options
import os
import random
from  match  import *
import time

#定义端口配置
define('port', type=int, default=8080)

#创建视图处理器
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class showHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        pics=self.request.files.get('picture',[])
        filename=pics[0]['filename']+str(time.time())
        save_path='./{}'.format(filename)
        print(save_path)
        with open (save_path,'wb+') as f:
            f.write(pics[0]['body'])
        
        res=match(filename)

        self.write(str(res))

#创建路由表
urls = [(r"/show", showHandler),(r"/chou", MainHandler)]

#创建配置-开启调试模式
configs = dict(debug=True)

#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls, configs):
        super(MyApplication, self).__init__(handlers=urls, **configs)

#创建服务器
def make_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(MyApplication(urls,configs))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

#启动服务器
if __name__ == '__main__':
    make_app()