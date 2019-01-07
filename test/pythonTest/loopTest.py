##############################
# print('水果循环')
# fruits=['apple','orange','banana','watermallon']
# for fruit in fruits:
   # print(fruit)
###############################
# print('数字循环')
# print(list(range(5)))
################################
# print('数字循环')
# for i in range(5):
   # print(i)
###############################
# print('数字循环')
# for i in list(range(5)):
   # print(i)
################################
# print('hello 循环')
# for name in ['Jay','Cat','Fat']:
   # print('hello',name)
# print('hello循环')
# for name in ['Jay','Cat','Fat']:
   # print('hello%s' % name)
################################
# print('计算1~100的和')
# sum=0
# for i in range(101):
   # print(i)
   # sum+=i
# print('1~100的和为',sum)
##################################
# print('while循环计算1~100的和')
# sum=0
# begin=100
# while begin>0:
   # sum+=begin
   # print(begin)
   # begin=begin-1
# print('while循环计算1~100的和为',sum)
##################################
# print('1-100的while循环50后break')
# begin=1
# while begin<=100:
   # print(begin)
   # begin=begin+1
# print('no break')
# begin=1
# while begin<=100:
   # print(begin)
   # if begin==50:
      # print('break')
      # break
   # begin=begin+1
# print('have break')
##################################
# print('1-100的while循环偶数continue')
# begin=0
# while begin<=100:
   # begin=begin+1
   # print(begin)
   # if begin%2:
      # print('continue')
      # continue   
# print('have continue')
##################################
print('打印九九乘法表')
res=''
i=9
list=[]
while i>0:
   list.append(i)
   i=i-1
for left in list:
   for right in list:
      if(right>=left):
         res=res+'  '+('%d * %d = %2d' % (left,right,left*right))
   res=res+'\n'
print(res)
res=''
for left in range(1,10):
   for right in range(1,10): 
      if(right>=left):
         res=res+'  '+('%d * %d = %2d' % (left,right,left*right))
   res=res+'\n'
print(res)


   









