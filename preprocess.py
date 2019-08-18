#!/usr/bin/python3
# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
# 从xml文件中读取，用getroot获取根节点，根节点也是Element对象
def process_xml_to_ontonotes(source_path,target_path):  # change  xml to the format of  ontonotes
    count_sentence = 0
    type_str = ''
    list_type = []
    tree = ET.parse(source_path)
    root = tree.getroot()
    # print(root)
    # print(root.tag,root.text)
    with open(target_path,'w',encoding='utf-8') as precess_text:
        for child in root:    # root is text
            for i in child:   # child is sentence,i is w
                # print(i.text, i.tag, i.attrib, i.tail)
                if not i.text is None:
                    precess_text.write(i.text+'\t'+ 'none'+'\t'+ 'none'+'\t'+'O'+'\n')
                    pass
                for j in i:   # i is w ,so j is NaMEX     <NAMEX TYPE="ORGANIZATION">中共中央</NAMEX>
                    precess_text.write(j.text+'\t'+ 'none'+ '\t'+'none'+'\t'+'B-'+j.attrib.get('TYPE')+'\n')
                    # print(j.text,j.tag,j.attrib.get('TYPE'),j.tail)  #中共中央 NAMEX {'TYPE': 'ORGANIZATION'} None   <w><NAMEX TYPE="ORGANIZATION">中共中央</NAMEX></w>
                    list_type.append(j.attrib.get('TYPE'))
            precess_text.write('\n')
            count_sentence= count_sentence +1
    set_types = set(list_type)
    f = open("./output_result/coun_train_mrsa.txt",'w')
    i = 0
    for one in set_types:
        i = i+1
        num_type = list_type.count(one)
        f.write(str(i)+":the type is "+one+":"+str(num_type)+"\n")
        print(str(i)+"the type is "+one+":"+str(num_type))      # count the num of   every kind of type for mrsa
        f.close()

    # print('The number of sentence is:')
    # print(count_sentence)
    # print('The number of typ is:')
    # print(len(set_types))


def count_enity(source_path,target_path):  # count the num  of mrsa.test.net's enities
    with open(source_path,'r+',encoding='utf-8') as file:
        tag = 1
        sentence_num = 0
        enity_list = []
        for line in file:
            line_list = line.split()
            line_len = len(line_list)
            if line_len == 0 and tag == 1:  # note: 'else' is logic error ,'elif' is correct
                tag = 0
                sentence_num = sentence_num + 1
            elif line_len == 4:
                tag = 1
                if line_list[3] not in 'O':
                    if line_list[3].__contains__('B-'):
                        enity_list.append(line_list[3])
            elif line_len != 0:
                tag = 1
    enity_set = set(enity_list)
    f = open(target_path, 'w')
    i = 0
    for one in enity_set:
        i= i+1
        num_type = enity_list.count(one)
        f.write(str(i) + ":the type is " + one + ":" + str(num_type) + "\n")
    f.close()
    print('The number of sentences:')
    print(sentence_num-1)
    print('The num of enity:')
    print(len(enity_list))
    print('The kinds of enity:')
    print(len(set(enity_list)))

if __name__ == '__main__':
    # process_xml_to_ontonotes('msra_bakeoff3_training.xml','./output_result/result.net')
    # count_enity("ontonotes_5.0/onto.test.ner","./output_result/coun_test_notonotes.txt")
    count_enity("msra/mrsa.development.ner","./output_result/count_development_mrsa.txt")
