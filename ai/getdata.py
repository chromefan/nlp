# -*- coding: UTF-8 -*-


import pymysql
import random
from words.Words import Words

# 连接配置信息
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'db': 'db',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}


def select(train_path):
    train_dir = open(train_path, 'w', encoding='utf-8')
    word = Words()
    db = pymysql.connect(**config)
    cur = db.cursor()
    # SQL 插入语句
    sql = "SELECT * FROM  text_class"
    cur.execute(sql)
    results = cur.fetchall()
    for textClass in results:
        cate_name = textClass['cate_name']
        cate_key = textClass['cate_key']
        sql = "SELECT * FROM text_set WHERE cate_key = '" + cate_key + "'"
        cur.execute(sql)
        text_sets = cur.fetchall()
        words_str = ''
        for texts in text_sets:
            text = texts['text']
            words_str += " "+word.cut_words(text)

        train_dir.write(cate_name + '||' + words_str)
        train_dir.write('\n')
        train_dir.flush()

    db.close()
    return results

# 生成训练样本
def generate_sample(dataList, labelList, trainPath, testPath):
    # 取30%作为测试集
    RATE = 0.3
    listLen = len(dataList)
    testLen = int(RATE * listLen)

    trainDir = open(trainPath, 'w', encoding='utf-8')
    testDir = open(testPath, 'w', encoding='utf-8')
    indexList = random.sample([i for i in range(listLen)], listLen)

    for item in indexList[:testLen]:
        testDir.write(labelList[item] + '||' + dataList[item])
        testDir.write('\n')
        testDir.flush()
    for item in indexList[testLen:]:
        trainDir.write(labelList[item] + '||' + dataList[item])
        trainDir.write('\n')
        trainDir.flush()


if (__name__ == '__main__'):

    trainPath = u'./datasets/trainsets/trainData.txt'
    text_class = select(trainPath)
    print(text_class)
