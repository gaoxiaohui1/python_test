class Stud(object):

   @property
   def name(self):
      return self._name
	  
   @name.setter
   def name(self,name):
      self._name=name
		
   @property
   def birthYear(self):
      return self._birthYear

   @birthYear.setter
   def birthYear(self,birthYear):
      if isinstance(birthYear,int):
         raise ValueError('birthYear must be a number')
      elif birthYear<0 or birthYear>2017:
         raise ValueError('birthYear must between 0~2017')
      else:
         self._birthYear=birthYear
		 
   @property
   def age(self):
      self._age=2017-self._birthYear
      return self._age


#######################################	  
class Stu(object):

   def __init__(self,name):
      self.name=name
	  
   def __getattr__(self,attr):
      if attr=='age':
         return 12
      raise AttributeError('Stu object has no attribute \'%s\'' % attr)
	  
	  
	  
#######################################
class Chain(object):

   def __init__(self,path=''):
      self._path=path

   def __getattr__(self,path):
      return Chain('%s/%s' % (self._path,path))
	  
   def __str__(self):
      return self._path
	  
   __repr__=__str__
