import os
import pandas as pd
import jieba as jb
import jieba.analyse as ana

class cutwords():

    _test_set_path = '../data/AutoMaster_TestSet.csv'
    _train_set_path = '../data/AutoMaster_TrainSet.csv'
    _column =  ['Question', 'Dialogue']
    _stopwords = '../data/stopwords/merge.txt'

    def __init__(self):
        self._test = pd.read_csv(self._test_set_path, encoding='utf-8')
        self._train = pd.read_csv(self._train_set_path, encoding='utf-8')
        self._load_stopwords()

    def _load_stopwords(self):
        if os.path.isfile(self._stopwords):
            ana.set_stop_words(self._stopwords)

    def cut_words(self, sentence):
        return ana.extract_tags(sentence)

if __name__ == '__main__':
    sentence = '您好，问汽车哪些部位，需要用高强度螺丝。哪些部位用普通螺丝代替?'
    cut = cutwords()
    data = cut.cut_words(sentence)
    print(data)
    print(jb.lcut(sentence))