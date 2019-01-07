
class Animal(object):
   def run(self):
      print('Animal is running ...')
	  
class Dog(Animal):
   def eat(self):
      print('Dog is eating...')
	  
class Cat(Animal):
   def run(self):
      print('Cat is running...')
   def sleep(self):
      print('Cat is sleeping...')
	  
class Duck(object):
   def run(self):
      print('Duck is running ...')
	 
def duck_like_test(obj):
   obj.run()

	  
	  
animal=Animal()
dog=Dog()
cat=Cat()	  
animal.run()
dog.run()
cat.run()
dog.eat()
cat.sleep()
duck=Duck()
print('-----duck like test-----')
duck_like_test(animal)
duck_like_test(dog)
duck_like_test(cat)
duck_like_test(duck)