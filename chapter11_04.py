#class 예제 4

class Dog: #모든 클래스는 object를 상속 받는다
   # 클래스 속성
   species ='firstdog'

   #초기화/ 인스턴스 속성
   #자바의 생성자와 비슷한 파이썬의 문법
   def __init__(self, name, age):#초기에 무조건 넘어오는 init 과 self
       self.name = name
       self.age = age

   def speak(self, sound):
       return "{} says {}!".format(self.name, sound)
    
   def info(self):
       return "{} is {} years old".format(self.name, self.age)

c = Dog('july', 4)
d = Dog('kk', 10)

print(c.info())

print(c.speak('wal wal'))