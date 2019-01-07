def stringIO_test():
   from io import StringIO
   s=StringIO()
   s.write('hello')
   s.write('\nworld')
   print(s.getvalue())
   
def stringIO_test1():
   from io import StringIO
   f=StringIO('aaaa\nbbbbb\nddddd\neeeeeee')
   print('...begin...')
   while True:
      s=f.readline()
      if s=='':
         print('...end...')
         break
      print('...ing...')
      print(s)	  

def renamefiles():
   import io
   pics=os.listdir('C:\\Users\\User\\Pictures\\Camera Roll')
   jpgs=[x for x in pics if '.jpg' in x.lower()]
	  
if __name__=='__main__':
   stringIO_test()
   stringIO_test1()
   