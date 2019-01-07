class Animal(object):
   def live(self):
      print('Animal live')
	  
class Mammal(Animal):
   def born(self):
      print('Mammal borned in body-way')
	  
class Bird(Animal):
   def born(self):
      print('Bird borned in egg_way')
	  
class RunnableMixIn(object):
   def run(self):
      print('running...')
	  
class FlyableMixIn(object):
   def fly(self):
      print('flying...')
	  
class TalkableMixIn(object):
   def talk(self):
      print('talking...')
	  
class Dog(Mammal,RunnableMixIn):
   def talk(self):
      print('wang wang wang...')
	  
class Bat(Bird,FlyableMixIn):
   def talk(self):
      print('ji ji ji...')
	  
# d=Dog()
# d.live()
# d.born()
# d.run()
# d.talk()
class Father(object):
   def hit(self):
      print('Father is hitting son...')
	  
class StepFather(object):
   def hit(self):
      print('StepFather is hitting son...')
	  	  
class LaoWang(object):
   def hit(self):
      print('LaoWang is hitting son...')
	  
class W1(Father,StepFather,LaoWang):
   pass
   
class W2(StepFather,Father,LaoWang):
   pass
   
class W3(LaoWang,StepFather,Father):
   pass
   
w1=W1()   
w2=W2()
w3=W3()
w1.hit()
w2.hit()
w3.hit()
