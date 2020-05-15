# -*- coding: utf-8 -*-
# @Time    : 4/11/20 10:24 PM
# @Author  : WEY
# @File    : count_sentences
# @Software: PyCharm


# def count_sen(path):
#     with open(path, 'r+', encoding='utf-8') as file:
#         i = -1
#         tag = 0
#         index_loc = 0
#         index_person = 0
#         index_org = 0
#         for line in file:
#             if line != '\n':
#                 tag_str = line.split()[1]
#                 if tag_str == 'B-LOCATION':
#                     index_loc = index_loc + 1
#                     # tag_start = tag_str.split('-')[0]
#                     # tag_end = tag_str.split('-')[1]
#                     # if tag_end == ''
#                 if tag_str == 'B-PERSON':
#                     index_person = index_person + 1
#                 if tag_str == 'B-ORGANIZATION':
#                     index_org = index_org + 1
#
#             if '\n' == line and tag == 0:
#                 i = i + 1
#                 tag = 1
#             else:
#                 tag = 0
#         print(path, i)
#         print("LOC>>>>>>>>>>>>>>>", path, index_loc)
#         print("PERSON>>>>>>>>>>>>>>>", path, index_person)
#         print("ORG>>>>>>>>>>>>>>>", path, index_org)
#
#
#
# if __name__ == '__main__':
#     path1 = '/home/zutnlp/corpus/mrsa/ner_test'
#     path2 = '/home/zutnlp/corpus/mrsa/ner_train'
#     count_sen(path1)
#     count_sen(path2)
# home/zutnlp/wueryong/projects/github/sigle_file/data/weiboNER.conll.dev
def count_sen(path):
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 5682: invalid continuation byte
    # aad errors='ignore'
    # https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
    with open(path, 'r+', encoding='utf-8', errors='ignore') as file:
        i = 0
        tag = 0
        index_loc = 0
        index_person = 0
        index_org = 0
        line_num = 0
        for line in file:
            line_num = line_num + 1
            if line != '\n':
                try:
                    tag_str = line.split()[1]
                except IndexError:
                    print("The error in>>>>>>>>>>>>>>>>>>", line_num)
                else:
                    if tag_str == 'B-LOC':
                        index_loc = index_loc + 1
                        # tag_start = tag_str.split('-')[0]
                        # tag_end = tag_str.split('-')[1]
                        # if tag_end == ''
                    if tag_str == 'B-PER':
                        index_person = index_person + 1
                    if tag_str == 'B-ORG':
                        index_org = index_org + 1

            if '\n' == line and tag == 0:
                i = i + 1
                tag = 1
            else:
                tag = 0
        print(path, i)
        print("B-LOCACTION", index_loc)
        print("B-PERSON", index_person)
        print("B-ORG", index_org)


if __name__ == '__main__':
    # path1 = '/home/zutnlp/wueryong/projects/github/sigle_file/data/weiboNER.conll.dev'
    # path2 = '/home/zutnlp/wueryong/projects/github/sigle_file/data/weiboNER.conll.train'
    # path3 = '/home/zutnlp/wueryong/projects/github/sigle_file/data/weiboNER.conll.test'
    # count_sen(path1)
    # count_sen(path2)
    # count_sen(path3)
    path1 = 'C://Users/Administrator/Desktop/Chinese-NLP-Corpus-master/NER/MSRA/msra_test_bio.txt'
    path2 = 'C://Users/Administrator/Desktop/Chinese-NLP-Corpus-master/NER/MSRA/msra_train_bio.txt'
    # path3 = '/home/zutnlp/wueryong/projects/github/sigle_file/data/weiboNER.conll.test'
    count_sen(path1)
    count_sen(path2)
    # count_sen(path3)
