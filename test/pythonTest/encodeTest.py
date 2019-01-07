# -*- coding: utf-8 -*-
# print('中文')
# print('----------')
# print('中文的长度是',len('中文'))
# print('----------')
# print('zw的长度是',len('zw'))
# print('----------')
# print('中文的长度是：len(\'中文\')=',len('中文'))
# print('----------')
# print('My Name is %s,I\'m %d years old,I have $%f.' % ('G',28,28.23))
#--------------------------------------------------------------------------------
# name=input('输入你的名字：')
# age=int(input('输入你的年龄：'))
# birthYear=2017-age
# if birthYear>=2010:
   # print('%s是10后' % name)
# elif birthYear>=2000:
   # print('%s是00后' % name)
# elif birthYear>=1990:
   # print('%s是90后' % name)
# elif birthYear>=1980:
   # print('%s是80后' % name)
# else:
   # print('%s已经是老人家了' % name)
#--------------------------------------------------------------------------------
# from func_test import func_abs_checkInput
# ff=func_abs_checkInput
# t=input('输入')
# print('ff(输入)=',ff(t))

#--------------------------------------------------------------------------------
from func_test import str2float
print(str2float(input('输入：')))