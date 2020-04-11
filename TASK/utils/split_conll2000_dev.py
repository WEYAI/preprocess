#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sklearn.model_selection import train_test_split
def split_conll(src,target):
    with open(src, 'r+', encoding='utf-8') as file:
        # for line in file:
        #     line = file.readlines()++----------
        #     line_len = len(line)
        #     if line_len == 0:
        #         import random
        #         data = file.read().split('\n')
        #         random.shuffle(data)
        #         train_data = data[:50]
        #         test_data = data[50:]
        #         print(train_data)
        #         print(test_data)

        xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=0)

        print("test_data........"+xTrain)
if __name__ == '__main__':
    split_conll("/home/zutnlp/wueryong/projects/corpus/conll2000/train.txt","");