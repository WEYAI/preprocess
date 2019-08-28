#!/usr/bin/python3
# -*- coding:utf-8 -*-
def count_words(src):
    with open(src,'r+',encoding='utf-8') as src_file:
       for  line in src_file:
           list = line.split(' ')
           print(list)
if __name__ == '__main__':
    count_words('test')