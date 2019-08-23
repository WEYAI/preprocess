#!/usr/bin/bash
# -*- encoding=utf-8 -*-
def processWeiboToWord(source,target):
    word_str = ""
    flag = 1
    start =1
    jump = 1
    with open(source,'r+',encoding='utf-8') as process_text:
        with open(target, 'w+', encoding='utf-8') as out_file:
            for line in process_text:
                line_list=line.strip()
                line_len=len(line_list)
                # print('s')
                if line_len == 0:
                    if word_str != '':
                        out_file.write(word_str + '\t' + 'none' + '\t' + 'none' + '\t' + 'O' + '\n')
                        word_str = ''
                        start = 1                               # revert to begin ,prevent the repeat
                    out_file.write('\n')


                elif line_list[0] == '�' or line_list[1] == '�': # Handing illegal characters
                    pass
                elif line_len > 5:                               # the length of the enity  > 5
                    location_index = int(line_list[1])
                    if location_index == 0:                      # dealing with 0 in enity ,for  example ,李0  B-PER.NAM
                        if word_str != '':                       # pass the '  ' in the word_
                            out_file.write(word_str + '\t' + 'none' + '\t' + 'none' + '\t' + 'O' + '\n')
                            word_str = ''
                            jump = 0                             # prevent to write again
                    out_file.write(line_list[0]+'\t'+'none'+'\t'+'none'+'\t'+line_list[3:]+'\n') # don't  include 1 ,like [ ).
                elif line_len < 5 or line_len == 5 :    # and 'O' in line_list[3]
                    location_index = int(line_list[1])
                    if start == 1:                   # at the start ,pass the the first '0'
                         word_str=word_str + line_list[0]
                         start = 0
                    else:                           # pass  the first '0',then meet the '0' , write the previous word
                        if location_index == 0 :
                            if jump == 1:
                                out_file.write(word_str + '\t' + 'none' + '\t' + 'none' + '\t' + 'O' + '\n')
                                word_str = ''       # clear the str
                            word_str = word_str + line_list[0]
                            jump = 1                # allow writing  the word
                        else:                       # if  the digital  != 0  ,like 1,2,3,4......
                            word_str = word_str +line_list[0]

if __name__ == '__main__':
    processWeiboToWord('weiboNER_2nd_conll.test' , 'weiboNET_2nd_conll.test.resust')
    processWeiboToWord('weiboNER_2nd_conll.train', 'weiboNET_2nd_conll.train.resust')
    processWeiboToWord('weiboNER_2nd_conll.dev', 'weiboNET_2nd_conll.dev.resust')



