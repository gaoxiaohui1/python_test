class Student(object):

   def __init__(self,name,age,gender,score):
      self.name=name
      self.age=age
      self.gender=gender
      self.score=score
	  
   def print_info(self):
      print('姓名：',self.name,';年龄：',self.age,';性别：',self.gender,';分数：',self.score)

def CreateStudent():
   name=input('请输入学生名字：')
   age=input('请输入学生年龄：')
   gender=input('请输入学生性别：')
   score=input('请输入学生分数：')
   return Student(name,age,gender,score)
   
def IsContinue(type=0):
   info='是否继续录入学生信息？（Yes\\No）'
   if type==1:
      info='是否继续查询学生信息？（Yes\\No）'
   v=input(info)
   if v!='Yes' and v!='No':
      print('只能输入【Yes】或【No】')
      IsContinue(type)
   else:
      return v=='Yes'


list=[]
list.append(CreateStudent())
isContinueInput=IsContinue()
while isContinueInput:
   list.append(CreateStudent())
   isContinueInput=IsContinue()
   
isContinueSearch=IsContinue(1)
searchName=''
while isContinueSearch:
   searchName=input('请输入想要查找的名字：')      
   resList=[x for x in list if x.name==searchName]
   if len(resList)==1:
      resList[0].print_info()
   else:
      print('未找到对应信息')
   isContinueSearch=IsContinue(1)


