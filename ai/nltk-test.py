#encoding=utf-8
import nltk
from nltk.corpus import names
import random

def gender_features(word): #特征提取器
    return {'last_letter':word[-1]} #特征集就是最后一个字母

names = [(name,'male') for name in names.words('./data/male.txt')]+[(name,'female') for name in names.words('./data/female.txt')]
random.shuffle(names)#将序列打乱

features = [(gender_features(n),g) for (n,g) in names]#返回对应的特征和标签

train,test = features[500:],features[:500] #训练集和测试集
classifier = nltk.NaiveBayesClassifier.train(train) #生成分类器

print('Neo is a',classifier.classify(gender_features('Neo')))#分类

print(nltk.classify.accuracy(classifier,test)) #测试准确度

classifier.show_most_informative_features(5)#得到似然比，检测对于哪些特征有用