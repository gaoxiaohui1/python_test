class Dict(dict):
   
   def __inti__(self,**kw):
      super().__init__(**kw)
	  
   def __getattr__(self,key):
      try:
         return self[key]
      except KeyError:
         raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
		 
   def __setattr__(self,key,value):
      self[key]=value
	  
import unittest

class TestDict(unittest.TestCase):
   
   def test_init(self):
      d=Dict(a=1,b='test')
      self.assertEqual(d.a,1)
      self.assertEqual(d.b,1)
      self.assertEqual(d.b,'test')
      print('...test_init...')
	  
   def test_key(self):
      d=Dict()
      d['asd']=123
      self.assertEqual(d.asd,123)
      print('...test_key...')
	  
   def setUp(self):
      print('test begin...')
	  
   def tearDown(self):
      print('test end...')
	  
	  
if __name__=='__main__':
   unittest.main()