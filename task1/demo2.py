# ! /usr/bin/python
# -*-coding:UTF-8-*-
import openpyxl
import re
import xlsxwriter
import io
def write_excel_xlsx(path, sheet_name, value): #path 存储xsls的路径 ，sheet_name 表名无需在意，  value 为二维列表
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    print("write_excel.11111..............................")
    for i in range(0, index):
        for j in range(0, len(value[i])):
            # if str(value[i][j]).__eq__('EOT'):
            # print("value>>>>>>>>>>>>>",value[i][j])
            temp = str(value[i][j]).replace('、',',')
            value[i][j] = temp
            temp0 = str(value[i][0]).replace('\x04','') #  疑问：r取消\的特殊含义,为什么加上r后就切换替换不成功。
            temp3 = str(value[i][3]).replace('\x04', '')#  为什么 temp3加上。
            value[i][0] = temp0
            value[i][3] = temp3

            print('第几行.............',i)
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]).encode('utf-8',errors='ingnore'))
    workbook.save(path)
    print("xlsx格式表格写入数据成功！")
def convert_to_doublelist(path):
        row_sigle = [] #单行
        rows = []      #对应多行xsls 数据 ，如  [[text1,text2,text3,text4],[text1,text2,text3,text4]............]嵌套列表即二维列表
        with open(path, "r", encoding="UTF-8",errors='ignore') as file:  #gb18030 是gbk 的超集，更大的解码范围。

            column1 = ''  # 单个文本的原文
            column2 = ''  # 单个文本的肿瘤原发部位
            column3 = ''  # 单个文本的原发病灶
            column4 = ''  # 单个文本的转移部位
            column2_index = 0
            column3_index = 0
            column4_index = 0

            rows.append(['原文', '肿瘤原发部位', '原发病灶大小', '转移部位'])
            for line in file:
                # print(">>>>>>>>>>>",line)
                predict_list = line.split()     # 以空格切分
                line_len = len(predict_list)    # 每行的列表的长度
                if (line_len == 2):
                    column1 = column1 + predict_list[0]
                    if(predict_list[1].__eq__("B-primary_focus") and column2_index<1):
                        column2_index = column2_index + 1
                        column2 = column2 + predict_list[0]
                    elif ( (predict_list[1].__eq__("I-primary_focus") or predict_list[1].__eq__("B-primary_focus"))  and column2_index<2 ):
                        column2 = column2 + predict_list[0]
                    if(predict_list[1].__eq__("B-tumor_size") and column3_index<1):
                        column3_index = column3_index + 1
                    elif ((predict_list[1].__eq__("B-tumor_size") or predict_list[1].__eq__("I-tumor_size")) and column3_index<2):
                        column3 = column3 + predict_list[0]
                    if(predict_list[1].__eq__("B-transfer_area") and column4_index<1):
                         column4_index = column4_index +1
                    elif ((predict_list[1].__eq__("B-transfer_area") or predict_list[1].__eq__("I-transfer_area")) and column4_index<2):
                        column4 = column4 + predict_list[0]
                elif (line_len.__eq__(0)):      #代表一个文本的结束
                    row_sigle.append(column1)
                    row_sigle.append(column2)
                    row_sigle.append(column3)
                    row_sigle.append(column4)
                    column1 = ''                # 清空
                    column2 = ''                # 清空
                    column3 = ''                # 清空
                    column4 = ''                # 清空
                    rows.append(row_sigle[:])  # 拒绝浅拷贝
                    row_sigle.clear();
                    column2_index = 0
                    column3_index = 0
                    column4_index = 0
        return rows
def main():
    sheet_name_xlsx = 'ceshi'
    read_path=r'final_predict_task1_2_after_transfer.txt'
    write_path='ceshi6.xlsx'
    rows = convert_to_doublelist(read_path)
    print(">>>>>>>>>>>>")
    write_excel_xlsx(write_path, sheet_name_xlsx, rows)

if __name__ == '__main__':
    main()
