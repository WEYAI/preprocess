#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File     : ontonoes
# @Author   : 张志毅
# @Time     : 2020/4/12 11:25
with open('/home/zutnlp/corpus/CoNLL-2003/eng.train', 'r',
          encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        temp = line.split()
        with open('/home/zutnlp/corpus/CoNLL-2003/eng.ner.train', 'a', encoding='utf-8') as af:
            if len(temp) != 0:
                af.write('{} {}\n'.format(temp[0], temp[3]))
            else:
                af.write('\n')
                # print(temp[0])
            # print('\n')
