#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File     : ontonoes
# @Author   : 张志毅
# @Time     : 2020/4/12 11:25
with open('E:\AI资料\ontonotes_5.0_chinese_dataset(1)\ontonotes_5.0_chinese_dataset\onto.test.ner', 'r',
          encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        temp = line.split()
        with open('E:\AI资料\ontonotes_5.0_chinese_dataset(1)\corpus\ontonotes_test.txt', 'a', encoding='utf-8') as af:
            if len(temp) != 0:
                af.write('{}    {}\n'.format(temp[0], temp[3]))
            else:
                af.write('\n')
                # print(temp[0])
            # print('\n')
        af.close()
    f.close()
