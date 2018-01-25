#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 连接配置信息
config = {
          'host': '127.0.0.1',
          'port': 3306,
          'user': 'root',
          'password': 'Luohj@2017',
          'db': 'cezi',
          'charset': 'utf8mb4',
          'cursorclass': pymysql.cursors.DictCursor,
}





def select(table):
    list = [0]
    db = pymysql.connect(**config)
    cur = db.cursor()
    # SQL 插入语句
    sql = "SELECT * FROM  " + table
    cur.execute(sql)
    results = cur.fetchall()
    for textClass in results:
        catename = textClass['cate_name']
        catekey = textClass['cate_key']
        sql = "SELECT * FROM text_set WHERE cate_key = '"+catekey+"'"
        cur.execute(sql)
        text_sets = cur.fetchall()
        for texts in text_sets:
            words = texts['text']
            print(words)
            exit()
    db.close()
    return results



if (__name__ == '__main__'):
    text_class = select('text_class')
    print(text_class)
