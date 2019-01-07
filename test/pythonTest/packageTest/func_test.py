def func_ABS(a):
   if(a>=0):
      return a
   else:
      return 0-a
def func_abs_checkInput(a):
	if not isinstance(a,(int,float)):
	   raise TypeError('只能传入数字')
	if a>0:
	   return a
	else:
	   return 0-a
def func_double(a):
   if not isinstance(a,(int,float)):
      raise TypeError('请输入数字')
   return int(a)*2

#返回多个结果
def func_tuple(a,b,c):
   a=a*2
   b=b*3
   c=c*4
   return (a,b,c)
   
#返回多个结果_找出小数点的位置和是否是正数   
def str2float(value):   
    dot = 0
    positive = 1  # 记录是否是正数
    if value[0] == '-':
        positive = -1
        value = value[1:] # 运用切片的知识

    for i in range(len(value)): # 遍历找出小数点的位置
        if value[i] == '.':
            value = value[:i] + value[i+1:] # 移除小数点
            dot = len(value) - i # 记录小数点的位置
            break
    return dot, positive, value  # 返回多个值
   
#默认参数
def func_defaultParam(a,b=2):
   res=1
   while b>0:
      res=res*a
      b=b-1
   return res
   
#可变参数
def func_varParam(*list):
   res=0
   for i in list:
      res=res+i
   return res
   
#关键字参数
def func_keyParam(name,age,**other):
   print('name:',name,'age:',age,'other:',other)
   
#命名关键字参数
def func_nKeyParam(name,age,*,addr,gender):
   print('name:',name,'age:',age,'addr:',addr,'gender:',gender)
   
#混合参数_参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def func_multParam(a,b,c=123,*args,**kw):
   print('a:',a,'b:',b,'c:',c,'args:',args,'kw:',kw)
   
#递归函数
def func_recursion(n):
   if n==1:
      return n
   else:
      return n+func_recursion(n-1)
	  
#汉诺塔_有三根相邻的柱子，标号为A,B,C，A柱子上从下到上按金字塔状叠放着n个不同大小的圆盘，要把所有盘子一个一个移动到柱子C上，并且每次移动同一根柱子上都不能出现大盘子在小盘子上方，请问至少需要多少次移动
def func_Hanoi(n,a,b,c):
   if n==1:
      print(a+str(n)+'--->'+c)
   else:
      func_Hanoi(n-1,a,c,b) #将A柱的n-1个盘移到B柱
      print(a+str(n)+'--->'+b)
      func_Hanoi(n-1,b,a,c) #将过渡柱子B上n-1个圆盘B移动到目标柱子C
      print(b+str(n)+'--->'+c)



def hanoi(n,x,y,z):
   if n==1:
      print(x,'-->',z)
   else:
      hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上	  
      hanoi(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
      hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上

#斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到	  
def func_fib(max):
   n,a,b=0,0,1
   while n<max:
      print(b)
      a,b=b,a+b
      n=n+1
   print('done')
   
def func_str2int(a,b=0):
   try:
      return int(a)
   except:
      return b
	  
	  
#函数作为参数
def func_sum_func(start,end,handle):
   sum=0
   for i in range(start,end+1):
      sum+=handle(i)
   return sum
def func_sum_func_handle(n):
   return n
   
#函数里面定义函数，相当于private不能import并且只能在调用前定义
def func_sum_func1(start,end):
   def func_sum_func1_handle(n):
      return n
   sum=0
   for i in range(start,end+1):
      sum+=func_sum_func1_handle(i)
   return sum
   
#高阶函数：函数作为参数
def func_highLevlefunc(a,*args):
   l=[]
   for func in args:
      try:
         l.append(func.__name__+'('+str(a)+')='+str(func(a)))
      except:
         l.append(func+'('+str(a)+')=undefined')
   print(l)
   
#闭包
def func_b_sum(args):
   def sum():
      a=0
      for i in range(0,args):
         a=a+i
      return a
   return sum

#报错
def func_b_sum1(args):
   def sum():
      a=0
      while args>0:
         a=a+args
         args=args-1
      return a
   return sum
# f1=func_b_sum1(10)

#报错_修改(内部函数可以使用但不能修改)
def func_b_sum2(args):
   def sum():
      a=0
      b=args
      while b>0:
         a=a+b
         b=b-1
      return a
   return sum


   
#闭包
def func_lazySum(*args):
   def sum():
      a=0
      for i in args:
         a=a+i
      return a
   return sum




















   