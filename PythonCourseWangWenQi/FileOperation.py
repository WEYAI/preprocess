#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pickle
import struct
#  def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
# Why does mode and no mode have the same effect
with open('ErrorData/1301001.dat', 'r+', encoding='gbk') as file:
    with open('ErrorData/senquence.txt', 'w+', encoding='utf-8') as output:
        # i = 0
        # while True:
        #     i = i+1
        #     lines = file.readline()
        #     line_char = lines.split()
        #     if i == 1:
        #         a,b,c,d = struct.unpack()
        #     # print(lines)
        #     print(line_char)
        #     if lines == '':
        #           break

        for line in output:
            print(line)
            # line_cols = line.split()
            # print("linechar ...",line_cols)
        #
        #
        #     # pickle.dump(line_char, output)
        #     # print(line_char)
        #     line_len = len(line)



    # print(data)
    # dataFile.write("test for write...............")
    # print(data)
