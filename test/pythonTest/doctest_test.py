def abs_test(n):
   '''
   demo
   
   >>> abs_test(1)
   1
   >>> abs_test(-1)
   -1
   >>> abs_test(1) 
   1
   >>> abs_test(-1) 
   1
   >>> abs_test(-2) 
   1
   '''
   return n
   
   
if __name__=='__main__':
   import doctest
   doctest.testmod()