#!/Users/luohuanjun/Applications/anaconda/anaconda/bin/python
# encoding=utf-8
'''
Created on 2016年6月25日

@author: lenovo
'''
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re
import random
import jieba
import joblib
import json
from tokenize import Ignore


class NBclassifier:
    def __init__(self, clf_path=None, vec_path=None):
        """
        创建对象时完成的初始化工作，判断分类器与vector路径是否为空，
        若为空则创建新的分类器与vector，否则直接加载已经持久化的分类器与vector。
        """
        if clf_path is None or vec_path is None:
            self.clf = MultinomialNB()
            self.vec = TfidfVectorizer()
        else:
            self.clf = joblib.load(clf_path)
            self.vec = joblib.load(vec_path)

    # 保存模型
    def save_model(self, clf_path="./datasets/trainModel/clf.m", vec_path="./datasets/trainModel/vec.m"):
        joblib.dump(self.clf, clf_path)
        joblib.dump(self.vec, vec_path)

    # 从文件夹中加载文本
    def load_texts(self, textPath):
        dirList = os.listdir(textPath)
        dataList = []
        labelList = []
        for dir in dirList:
            fileList = os.listdir(textPath + '/' + dir)
            for filename in fileList:
                line = open(textPath + u'/' + dir + u'/' + filename, encoding='utf-8', errors='ignore').read()
                line = re.sub(u'\t|\n', u'', line)
                if line != u'':
                    dataList.append(line)
                    labelList.append(dir)
                    #                     print(filename)
        dataList = self.jieba_split(dataList)
        return dataList, labelList

    # 载入数据集
    @staticmethod
    def load_data(dataPath):
        dataList = []
        labelList = []
        for line in open(dataPath, encoding='utf-8').readlines():
            lineArray = line.split('||')
            if (len(lineArray) == 2):
                labelList.append(lineArray[0])
                dataList.append(lineArray[1])
        print('长度是{0}'.format(len(dataList)))
        return dataList, labelList

    # 随机生成训练样本与测试样本
    @staticmethod
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

    # ds
    # 结巴分词

    @staticmethod
    def jieba_split(data):
        result = []
        # 首先利用结巴分词
        for content in data:
            line = ' '.join(jieba.cut(content))
            result.append(line)
        return result

    # 训练数据
    def train(self, dataList, labelList):
        # 训练模型首先需要将分好词的文本进行向量化，这里使用的TFIDF进行向量化
        self.clf.fit(self.vec.fit_transform(dataList), labelList)
        self.save_model()

    # 预测数据
    def predict(self, dataList, labelList):

        data = self.vec.transform(dataList)
        predictList = self.clf.predict(data)
        return predictList

    # 计算准确率
    @staticmethod
    def cal_accuracy(labelList, predictList):
        rightCount = 0
        if len(labelList) == len(predictList):
            for i in range(len(labelList)):
                if labelList[i] == predictList[i]:
                    rightCount += 1
            print('准确率为：%s' % (rightCount / float(len(labelList))))


if __name__ == '__main__':
    # 创建NB分类器
    nbclassifier = NBclassifier()
    # 数据集地址及生成的训练集与测试集地址
    # dataPath = u'./datasets/docsets'
    trainPath = u'./datasets/trainsets/trainData.txt'
    testPath = u'./datasets/testsets/testData.txt'
    # dataList, labelList = nbclassifier.load_texts(dataPath)
    # nbclassifier.generate_sample(dataList, labelList, trainPath, testPath)

    # 载入训练集与测试集
    dataList, labelList = nbclassifier.load_data(trainPath)
    testData, testLabel = nbclassifier.load_data(testPath)
    # 训练并预测分类正确性

    nbclassifier.train(dataList, labelList)
    predictList = nbclassifier.predict(testData, testLabel)
    nbclassifier.cal_accuracy(predictList, testLabel)
