def func_test(a):
   try:
      print('try...')
      r=10/int(a)
      print('result:',r)
   except ValueError as e:
      print('ValueError:',e)
   except ZeroDivisionError as e:
      print('ZeroDivisionError:',e)
   finally:
      print('finally...')
   print('end...')
  

if __name__=='__main__':  
   a=input('input a number:')
   func_test(a)