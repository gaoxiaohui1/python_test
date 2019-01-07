from enum import Enum

animal=Enum('animal',('Dog','Cat','Pig'))

for name,member in  animal.__members__.items():
   print(name,'=>',member,',',member.value)
   
   
   
from enum import Enum,unique

@unique
class EnumOperateType(Enum):
   Edit=10
   Save=20
   Submit=30
   Reviw=40
   Delete=50