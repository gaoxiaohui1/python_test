import moduleTest1
def testMax(*args):
   return(max(args))
v=moduleTest1.testAdd(3,4)
if __name__=='__main__':
   print('moduleTest2=',v)