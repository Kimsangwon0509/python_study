 #클래스 개념
 #OOP란
 #Self개념
 #인스턴스 메소드
 #클래스, 인스턴스 변수

# 예제1
#class Dog(object): 
#class Dog(): 
class Dog: #모든 클래스는 object를 상속 받는다
   # 클래스 속성
   species ='firstdog'

   #초기화/ 인스턴스 속성
   #자바의 생성자와 비슷한 파이썬의 문법
   def __init__(self, name, age):#초기에 무조건 넘어오는 init 과 self
       self.name = name
       self.age = age

# 클래스 정보 
print(Dog)

# 인스턴스화
a = Dog("mickey",2) #self는 자동으로 넘어온다
b = Dog("mung",3)
c = Dog("mung",3)
# 비교
print(a == b, id(a), id(b), id(c)) #인스턴스화 시킨것은 전부 다 다른다.

# 네임 스페이스
print('dog1', a.__dict__)
print('dog1', b.__dict__)

#클래스 와 인스턴스 차이이해
#네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능
#인스턴스 변수 : 객체마다 별도 존대

#인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

print(Dog.species)
print(a.species)
print(b.species)
