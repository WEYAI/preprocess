import numpy as np


def split_data(file, trian_file, valid_file):
    with open(trian_file, 'w', encoding='utf-8') as fw1:
        with open(valid_file, 'w', encoding='utf-8') as fw2:
            # with open(test_file, 'w', encoding='utf-8') as fw3:
                with open(file, 'r', encoding='utf-8') as fr:
                    data = fr.read().split('\n\n')
                    data_index = [i for i in range(len(data))]
                    np.random.shuffle(data_index)
                    rate = 0.9 # 按8：1:1拆分
                    len_train = int(rate * len(data))
                    len_valid = int(0.1 * len(data))
                    # len_test = int(0.1 * len(data))
                    # 训练
                    for i in range(len_train):
                        fw1.write(data[data_index[0]] + '\n' + '\n')
                        del data_index[0]
                    # 验证
                    for j in range(len_valid):
                        fw2.write(data[data_index[0]] + '\n' + '\n')
                        del data_index[0]
                    # 测试
                    # for k in range(len_test):
                    #     fw3.write(data[data_index[0]] + '\n' + '\n')
                    #     # del data_index[0]

path = "/data/zutnlp/sequence/msra_3_bioes"
path_read = path + '/bioes.msra.train.ner'
path_train = path +'/bioes.msra.train_split_train.ner'
path_dev = path +'/bioes.msra.train_split_dev.ner'
# path_test  = path + 
split_data(path_read, path_train, path_dev)
