import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # add the path or code access
# (os.path.dirname(os.path.abspath(__file__)) 'D:\\Projects\\github\\preprocess\\PythonCourseWangWenQi'
# os.path.abspath(__file__) 'D:\\Projects\\github\\preprocess\\PythonCourseWangWenQi\\split.py'
os.getcwd()  # get current directory # eg: 'D:\\Projects\\github\\preprocess\\PythonCourseWangWenQi'

if __name__ == '__main__':
    tag = 'B-LOC'
    list = ['B-LOC', 'B-PER', 'B-PER']
    new_list = []
    [new_list.append(i.split('-')[1]) for i in list if not i in new_list]
    # If () ,TypeError: 'list' object is not callable
    # [new_list.append(i.split('-')(1)) for i in list if not i in new_list]

    temp = tag.split('-')
    print(set(new_list))
    print(list[1])
