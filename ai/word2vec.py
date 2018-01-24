#encoding=utf-8
from gensim.models import word2vec

import sys

sentences = [['我哎', '你'], ['他们', '我爱你']]
model=word2vec.Word2Vec(sentences, min_count=1)

for i in model.most_similar(u"我你"):
    print (i[0],i[1])