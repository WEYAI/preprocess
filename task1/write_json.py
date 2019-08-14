import os, json, shutil

def read():
    result_dict = []
    filenames = os.listdir(os.path.join('.', 'rec_results'))

    fl = 1
    while fl<len(filenames)+1:
        path1 = os.path.join('.','test_data/record-'+str(fl)+'.txt')
        path2 = os.path.join('.','rec_results/record-'+str(fl)+'.txt')
        emr = ''
        with open(path1,encoding='utf-8') as fr1:
            lines = fr1.readlines()
            for line in lines:
                emr += line
        fr1.close

        sin_dict = {}
        sin_dict['originalText'] = emr
        sublist = []

        with open(path2, encoding='utf-8') as fr2:
            lines = fr2.readlines()
            entity_list = []
            for line in lines:
                line = line.strip()
                if len(line)>0:
                    entity_list.append(line.strip())

            if len(entity_list)>0:
                for el in entity_list:
                    entity, bpos, epos, category = el.split('\t')
                    dic = {}
                    dic['label_type'] = category
                    dic['overlap'] = 0
                    dic['start_pos'] = int(bpos)
                    dic['end_pos'] = int(epos)
                    sublist.append(dic)
        
        sin_dict['entities'] = sublist
        result_dict.append(sin_dict)
        
        fl += 1
    return result_dict

def write(dic_list):
    path = os.path.join('.','result.json')
    
    with open(path, 'w', encoding='utf-8') as fr:
        for dl in dic_list:
            json.dump(dl, fr, ensure_ascii=False)
            fr.write('\n')
    fr.close
        
if __name__=='__main__':
    dic_list = read()
    write(dic_list)
