import os
import sys

path = input("请输入文件路径:")
filename =input("请输入新的文件名称:")
suffix = input("请输入新的文件的后缀名:")

f = os.listdir(path)
n = 0

for each in f:
    old_name = path + each
    old_name_f = each
    new_name= path + filename + str(n + 1) + suffix
    new_name_f = filename + str(n + 1) + suffix

    os.rename(old_name,new_name)

    print(old_name_f , "------>" , new_name_f ,"成功")
    n += 1
