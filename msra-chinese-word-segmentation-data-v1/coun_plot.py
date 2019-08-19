# import matplotlib.pyplot as plt
# import numpy as np
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# plt.rcdefaults()
# fig, ax = plt.subplots()
#
# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# performance2 = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))
#
#
# total_width, n = 0.8, 2
# width = total_width / n
# y_pos=y_pos - (total_width - width) / 2
#
# b=ax.barh(y_pos, performance, align='center',
#         color='green', ecolor='black',height=0.2,label='a')
# #添加数据标签
# for rect in b:
#     w=rect.get_width()
#     ax.text(w,rect.get_y()+rect.get_height()/2,'%f'%w,ha='left',va='center')
#
# b=ax.barh(y_pos+width, performance2, align='center',
#         color='red', ecolor='black',height=0.2,label='b')
# #添加数据标签
# for rect in b:
#     w=rect.get_width()
#     ax.text(w,rect.get_y()+rect.get_height()/2,'%f'%w,ha='left',va='center')
# ax.set_yticks(y_pos+width/2.0)
# ax.set_yticklabels(people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Category_number')
# ax.set_title('Category')
# plt.legend()
# plt.show()
# # print(y_pos+3)
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#数据
name=['GPE','PERSON','DATE','ORG','CARDINAL','NORP','LOC','TIME','FAC','MONEY','ORDINAL','EVENT','WORK_OF_ART','QUANTITY','PERCENT','LANGUAGE','PRODUCT','LAW']
colleges=[15739,10694,8043,7954,6969,2493,1925,1481,1173,1161,1092,972,799,788,749,328,291,235]

#图像绘制
fig,ax=plt.subplots()
b=ax.barh(range(len(name)),colleges,color='#6699CC')

#添加数据标签
for rect in b:
    w=rect.get_width()
    ax.text(w,rect.get_y()+rect.get_height()/2,'%d'%int(w),ha='left',va='center')

#设置Y轴刻度线标签
ax.set_yticks(range(len(name)))
#font=FontProperties(fname=r'/Library/Fonts/Songti.ttc')
ax.set_yticklabels(name)
ax.set_xlabel('Category_number')
ax.set_title('Category')

plt.show()