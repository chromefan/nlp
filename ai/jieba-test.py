# encoding=utf-8
import jieba



jieba.load_userdict("./data/userdict.txt")

stopwords_file = "./data/stop_words.txt"

stop_f = open(stopwords_file,"r",encoding='utf-8')
stop_words = list()
for line in stop_f.readlines():
    line = line.strip()
    if not len(line):
        continue

    stop_words.append(line)
stop_f.close

print(len(stop_words))


seg_list = jieba.cut("比特币、以太坊，他来到了网易杭研大厦",cut_all=False)  # 默认是精确模式

outstr = ''
for word in seg_list:
    if word not in stop_words:
        if word != '\t':
            outstr += word
            outstr += "/"


print(outstr)

