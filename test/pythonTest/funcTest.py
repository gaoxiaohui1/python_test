########################
# a=float(input('a=输入想要知道绝对值的数：'))
# print('abs(a)=',abs(a))
# a=int(input('a=输入想要知道16进制结果的数：'))
# print('hex(a)=',hex(a))

########################
# def func_ABSTest(s):
   # if(s>=0):
      # return s
   # else:
      # return 0-s
	  
# a=int(input('a=输入想知道绝对值的数：'))
# print('func_ABSTest(a)=',func_ABSTest(a))
########################
# from func_test import func_ABS
# print('from func_test import func_ABS')
# a=int(input('a=输入想知道绝对值的数：'))
# print('func_ABS(a)=',func_ABS(a))
# from func_test import func_double
# a=input('a=输入想加倍的数：')  
# print('func_double(a)=',func_double(a))
########################
# from func_test import func_tuple
# a=int(input('input a number:'))
# b=float(input('input a number:'))
# c=int(input('input a number:'))
# print('func_tuple(a,b,c)=',func_tuple(a,b,c))
########################
# from func_test import func_defaultParam
# a=int(input('a=input number:'))
# b=int(input('b=input number:'))
# print('func_defaultParam(a,b)=',func_defaultParam(a,b))
# print('func_defaultParam(a)=',func_defaultParam(a))
########################
# a=input('a=input number:')
## print(is_integer(a))
# if a is int:
   # print(1)
# else:
   # print(2)
########################
# from func_test import func_varParam
# list=[]
# a=int(input('a=input number a:'))
# list.append(a)
# b=int(input('a=input number b:'))
# list.append(b)
# c=int(input('a=input number c:'))
# list.append(c)
# d=int(input('a=input number d:'))
# list.append(d)
# print(list)
# print('func_varParam(list)=',func_varParam(*list))
# print('list2=[4,3,2,1]')
# list2=[4,3,2,1]
# print('func_varParam(list2[0],list2[1],list2[2],list2[3])=',func_varParam(list2[0],list2[1],list2[2],list2[3]))
########################
# from func_test import str2float
# print(str2float(input('输入：')))
########################
# from func_test import func_varParam
# f_vp=func_varParam
# list=[1,2,3,4,5]
# print('f_vp(*list)=',f_vp(*list))

########################
# from func_test import func_keyParam
# f_kp=func_keyParam
# f_kp('John',12)
# f_kp('Bob',13,address='T Street',height=123)
# dic={'address':'A Street','height':132,'weight':50.0}
# f_kp('Nick',14,**dic)

########################
# from func_test import func_nKeyParam
# func_nKeyParam('G',28,addr='Street')
# func_nKeyParam('G',28,gender='male')
# func_nKeyParam('G',28,addr='Street',gender='male')
# func_nKeyParam('Error',12,address='addr')

########################
# from func_test import func_multParam
# f_mp=func_multParam
# list=[1,1.2,True,'asd',None]
# dic={'name':'GG','age':23,'height':175.5}
# f_mp('a','b')
# f_mp('a','b',456)
# f_mp('a','b',*list)
# f_mp('a','b',789,*list)
# f_mp('a','b',*list,**dic)
########################
# from func_test import func_recursion
# max=int(input('输入一个数值：'))
# s=''
# for i in range(max):
   # if(i!=0):
      # s+=str(i)+'+'
# print(s+str(max),'=',func_recursion(max))
########################
# from func_test import func_Hanoi
# n=int(input('输入一个数值：'))
# func_Hanoi(n,'A','B','C')
########################
# from func_test import hanoi
# n=int(input('输入一个数值：'))
# hanoi(n,'A','B','C')
########################
# from func_test import func_fib
# n=int(input('输入数字：'))
# func_fib(n)
########################
# from func_test import func_str2int
# a=input('输入：')
# print(func_str2int(a))
#########################
# from func_test import func_sum_func
# from func_test import func_sum_func_handle
# from func_test import func_sum_func1
# from func_test import func_sum_func1_handle
# print(func_sum_func(0,10,func_sum_func_handle))
# print(func_sum_func1(1,10))
#########################
# from func_test import func_highLevlefunc
# from math import tan
# from math import cos
# func_highLevlefunc(123,abs,tan,cos)
#########################
# from func_test import func_b_sum2
# f1=func_b_sum2(10)
# f2=func_b_sum2(10)
# print('f1:',f1)
# print('f2:',f2)
# print('f1==f2:',f1==f2)
# print('f1():',f1())
# print('f2():',f2())
# print('f1()==f2():',f1()==f2())
#########################
# from packageTest.func_test import func_b_sum2
# f1=func_b_sum2(15)
# f2=func_b_sum2(15)
# print('f1:',f1)
# print('f2:',f2)
# print('f1==f2:',f1==f2)
# print('f1():',f1())
# print('f2():',f2())
# print('f1()==f2():',f1()==f2())
#########################
# import packageTest.func_test
# func_b_sum2=packageTest.func_test.func_b_sum2
# f1=func_b_sum2(15)
# f2=func_b_sum2(15)
# print('f1:',f1)
# print('f2:',f2)
# print('f1==f2:',f1==f2)
# print('f1():',f1())
# print('f2():',f2())
# print('f1()==f2():',f1()==f2())
#########################
import sys
print(sys.argv)
print(__name__)















