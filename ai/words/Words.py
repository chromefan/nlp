# encoding=utf-8
import jieba


class Words:
    dictPath = ''

    def __init__(self):
        self.dictPath = './data/'

    def cut_words(self, text):
        jieba.load_userdict(self.dictPath + "userdict.txt")
        stopwords_file = self.dictPath + "stop_words.txt"
        stop_f = open(stopwords_file, "r", encoding='utf-8')
        stop_words = list()
        for line in stop_f.readlines():
            line = line.strip()
            if not len(line):
                continue
            stop_words.append(line)
        stop_f.close()

        seg_list = jieba.cut(text, cut_all=False)  # 默认是精确模式

        outstr = ''
        for word in seg_list:
            if word not in stop_words:
                if word != '\t':
                    outstr += word
                    outstr += " "

        return outstr

