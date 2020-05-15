#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File     : ontonoes
# @Time     : 2020/4/12 11:25
import os


def convert(source, target, dir):
    '''

    :param source:the source  file path
    :param target:the result file path
    :param dir: if the path don't exit create the directory
    :return:
    '''
    with open(source, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            if not os.path.exists(dir):
                os.makedirs(dir)
            with open(target, 'a', encoding='utf-8') as af:
                if len(temp) != 0:
                    af.write('{} {}\n'.format(temp[0], temp[3]))
                else:
                    af.write('\n')
                    # print(temp[0])
                # print('\n')


if __name__ == '__main__':
    convert('/home/zutnlp/corpus/notoNotes5.0/onto.development.ner',
            '/home/zutnlp/corpus/notoNotes5.0/ner/onto.development.ner', '/home/zutnlp/corpus/notoNotes5.0/ner')
    convert('/home/zutnlp/corpus/notoNotes5.0/onto.train.ner', '/home/zutnlp/corpus/notoNotes5.0/ner/onto.train.ner',
            '/home/zutnlp/corpus/notoNotes5.0/ner')
    convert('/home/zutnlp/corpus/notoNotes5.0/onto.test.ner', '/home/zutnlp/corpus/notoNotes5.0/ner/onto.test.ner',
            '/home/zutnlp/corpus/notoNotes5.0/ner')
