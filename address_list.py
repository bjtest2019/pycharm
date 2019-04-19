#_author:test
#date:2019/4/14

import pickle

address_list = [('1','增加'),('2','删除')]
print("""
------通讯录------
1.添加
2.查找
3.删除
4.修改
5.退出""")
while True:
 choice = input("请输入操作>>>:")
 if choice =='1':
     name = input("请输入姓名：")
     phone = input("请输入电话号码：")
     #record = Record(name,phone)
 if choice =='2':
     select = input("查找：")


 if choice =='1':
     name = input("请输入姓名：")
     phone = input("请输入电话号码：")

 if choice =='3':
     name_del = input("删除：")



