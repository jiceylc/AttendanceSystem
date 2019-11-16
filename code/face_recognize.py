# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options
import os
import random
from match import *
import time
import pymysql
from preprocess_page2base import *
import json


# 定义端口配置
define('port', type=int, default=8088)
print(str(options.port)+" is running")


# 创建视图处理器，首页
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        
# 登入界面


class LogHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('log.html')

# 添加用户


class UserAddHandler(tornado.web.RequestHandler):
    def post(self):
        id=self.get_body_argument("add_id")
        name=self.get_body_argument("add_name")
        pics = self.request.files.get('file', [])
        filename = "user_add"+str(time.time()) + ".jpg"
        save_path = './source/{}'.format(filename)
        print(id,name)
        with open (save_path,'wb+') as f:
            f.write(pics[0]['body'])
        # 保存用户头像模板
        head_url=preprocess(save_path,id)
        # print('INSERT INTO user (pwd,id,name,identity,head_img)VALUES("123456",'+id+','+name+','+'"stu",'+head_url+');')
        # 将用户存入数据库

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xtl980417', db='cv_kq')
        cursor = conn.cursor()
        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        cursor.execute('INSERT INTO user (pwd,id,name,identity,head_img)VALUES("123456",'+'"'+id+'"'+','+'"'+name+'"'+','+'"stu",'+'"'+head_url+'"'+');')
        conn.commit()
        cursor.close()
        conn.close()
        self.write("ok")


class UserDeleteHandler(tornado.web.RequestHandler):
    def post(self):
        id=self.get_body_argument("delete_id")
        print('delete from user where id ='+'"'+id+'";')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xtl980417', db='cv_kq')
        cursor = conn.cursor()
        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        cursor.execute(
            'delete from user where id ='+'"'+id+'";')
        conn.commit()
        cursor.close()
        conn.close()
        self.write("ok")


class UserSearchHandler(tornado.web.RequestHandler):
    def post(self):
        name=self.get_body_argument("search_name")
        search_date=self.get_body_argument("search_date")
        print(name,search_date)

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xtl980417', db='cv_kq')
        cursor = conn.cursor()
        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        if(name and search_date):
            print('select *  from kqb where name="'+name+'"and time='+'"'+search_date+'";')
            cursor.execute(
            'select *  from kqb where name="'+name+'"and time='+'"'+search_date+'";')
        elif(name and not search_date):
            cursor.execute(
            'select *  from kqb where name="'+name+'";')
        elif( search_date and not name  ):
            cursor.execute(
            'select *  from kqb where time="'+search_date+'";')
        else:
            cursor.execute(
            'select *  from kqb ;')

        result = cursor.fetchall()
        print(result)


        conn.commit()
        cursor.close()
        conn.close()
        ans=json.dumps(result)
        print(ans)

        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(ans)

        # self.write()





#检查用户名密码
class CheckHandler(tornado.web.RequestHandler):
    def get(self):
        username=self.get_argument("username")
        pwd=self.get_argument("passward")
        print(username,pwd)
        self.set_status(200) # 标准状态码，不用设置reason

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xtl980417', db='cv_kq')
        cursor = conn.cursor()

        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        effect_row = cursor.execute("select * from user  where id='"+username+"' and pwd='"+ pwd+"'")
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        print(result)
        if(result):
            print("验证成功")
            self.write("1")
        else:
            self.write('2')

class upload_tableHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        data=json.loads(self.request.body.decode("utf8"))
        print(len(data["upload_table"]),data["upload_table"][0]["name"])

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xtl980417', db='cv_kq')
        cursor = conn.cursor()

        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        for i in range(len(data["upload_table"])):
            name=str(data["upload_table"][i]["name"])
            if(str(data["upload_table"][i]["status"])=="False"):
                status="未签到"
            else:
                status="已签到"
            date_time=time.strftime("%Y-%m-%d", time.localtime())
            print(name,status,date_time,'INSERT INTO kqb (name,time,status)VALUES("'+name+'",'+'"'+status+'",'+'"'+date_time+'"'+');')

            cursor.execute('INSERT INTO kqb (name,time,status)VALUES("'+name+'",'+'"'+date_time+'",'+'"'+status+'"'+');')

        conn.commit()
        cursor.close()
        conn.close()

        self.write("1")




#处理人脸识别
class kq_checkHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        pics=self.request.files.get('kq_pic',[])
        filename = "qk"+str(time.time())+pics[0]['filename']
        save_path='./source/{}'.format(filename)
        # print (save_path)
        with open (save_path,'wb+') as f:
            f.write(pics[0]['body'])

        # print("save_path:",save_path)
        img_temp=detect(save_path)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xtl980417', db='cv_kq')
        cursor = conn.cursor()

        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        cursor.execute("select id,name,head_img from user ")
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        # print(result)

        head_img=[i[2] for i in result]
        name=[i[1] for i in result]

        print(head_img,name,img_temp)
        ans=recognition(head_img, name,img_temp)
        print(ans)
        ans=json.dumps(ans)

        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(ans)

#创建路由表
urls = [(r"/useradd", UserAddHandler),
        (r"/kq_check", kq_checkHandler),
        (r"/index", MainHandler),
        (r"/log", LogHandler),
        (r"/check",CheckHandler),
        (r"/upload_table", upload_tableHandler),
        (r"/usersearch", UserSearchHandler),
        (r"/userdelete",UserDeleteHandler)]

#创建配置-开启调试模式
configs = dict(debug=True,static_path=os.path.join(os.path.dirname(__file__), "static"))

#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls, configs):
        super(MyApplication, self).__init__(handlers=urls,  **configs)

#创建服务器
def make_app():
    tornado.options.parse_command_line()
    # tornado.web.Application(static_path)
    http_server = tornado.httpserver.HTTPServer(MyApplication(urls,configs))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

#启动服务器
if __name__ == '__main__':
    make_app()
