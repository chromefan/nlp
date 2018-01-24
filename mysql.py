#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import time

def read(io,num):
    list = [0]
    db = pymysql.connect(
        "127.0.0.1",
        "root",
        'Luohj@2017',
        'jet_data',
    )

    #conn = MySQLdb.connect(conn)
    # cursorclass 使输出变为字典形式
    cur = db.cursor()
    # SQL 插入语句
    sql = "INSERT INTO upload_test(file_name, \
           file_key, file_size,upload_time) \
           VALUES ( '%s', '%s', '%d', '%d' )" % \
          ( 'Mohan', 'key', 10, 2000)
    cur.execute(sql)


    print ("thread :%s" % (io))
    db.commit();
    db.close()
    time.sleep(1)

read('etest',1);
