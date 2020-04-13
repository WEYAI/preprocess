# -*- coding: utf-8 -*-
# @Time    : 4/11/20 10:24 PM
# @Author  : WEY
# @File    : count_sentences
# @Software: PyCharm


def count_sen(path):
    with open(path, 'r+', encoding='utf-8') as file:
        i = -1
        tag = 0
        line: str
        for line in file:
            if '\n' == line and tag == 0:
                i = i + 1
                tag = 1
            else:
                tag = 0
        print(path, i)


if __name__ == '__main__':
    path1 = '/home/zutnlp/corpus/notoNotes5.0/onto.train.ner'
    path2 = '/home/zutnlp/corpus/notoNotes5.0/onto.development.ner'
    path3 = '/home/zutnlp/corpus/notoNotes5.0/onto.test.ner'
    count_sen(path1)
    count_sen(path2)
    count_sen(path3)
