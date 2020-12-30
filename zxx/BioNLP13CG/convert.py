'''
Author: WEY
Date: 2020-12-30 18:47:40
LastEditTime: 2020-12-30 20:11:57
'''
import os
import sys
sys.path.append('../')
os.chdir(sys.path[0])
# CHEM (simple chemical)，CC (cellular component)，GGP (gene and gene product) ， SPE (species)->Organism，CELL (cell)
def convert(src_path,tgt_path):
   with open(src_path,'r+',encoding='utf-8') as src:
    with open(tgt_path,'w+',encoding='utf-8') as tgt:
        lines  = src.readlines()
        for line in lines:
            if line == '\n':
                pass
            else:
                text =  line.split('\t')[0]
                tag =  line.split('\t')[1]
            if 'Simple_chemical' in tag:
                pass
            elif 'Gene_or_gene_product' in tag:
                pass
            elif 'Cellular_component'  in tag:
                pass
            elif 'Cell' in tag:
                pass
            elif 'B-Organism'  or "I-Organism"  or "E-Organism" or "S-Organism" == tag :
                pass
            else:
                line = text +'\t' + 'O\n' 
            tgt.write(line)
convert("train.tsv","train01.tsv")
convert("dev.tsv","dev01.tsv")
convert("test.tsv","test01.tsv")