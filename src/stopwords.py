import os, sys

# 合并文件
def merge_file(outfile, infile):
    with open(outfile, 'r', encoding='utf-8') as f1:
        data = f1.readlines()

    with open(infile, 'a', encoding='utf-8') as f2:
        for line in data:
            f2.write(line)
        f2.close()

class stopwords:
    '''
    整理合并停用词
    '''
    def __init__(self):
        self._dir = '../data/stopwords/'
        self._merge_file = '../data/stopwords/merge.txt'

    def _merge_all_file(self):
        # 删除已经存在的合并文件
        if os.path.exists(self._merge_file):
            os.remove(self._merge_file)
        # 获取文件列表
        file_list = os.listdir(self._dir)
        # 合并文件
        for file in file_list:
            merge_file(self._dir + file, self._merge_file)

    # 获取停用词列表
    def read_merge_file(self):
        if not os.path.isfile(self._merge_file):
            self._merge_all_file()

        with open(self._merge_file, 'r', encoding='utf-8') as f:
            data = f.readlines()
        data = [line.strip() for line in data]
        return data

if __name__ == '__main__':
    word = stopwords()
    words = word.read_merge_file()
    print(words)