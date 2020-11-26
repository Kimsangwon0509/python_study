#파이썬 제어문
#IF 실습

# 기본 형식
print(type(True))
print(type(False))

# 예 1
if True:
    print('Good')


# 예 2
if False:
    print('Bad')
else:
    print('good')


# 관계 연산자
# <, <= ...
x = 15
y = 20
print(x == y)
print(x != y)
print(x >= y)
print(x < y)
print(x <= y)

city = ""
if city:
    print("You are in:", city)
else: 
    print("Please enter your City")

#논리 연산자
# and, or ,not

a = 75
b = 40
c = 10

print(a>b and b>c)
print(a>b or b>a)
print(a>b or b>c)
print(not a>b) 
print(not True) 

# 산술, 관계, 논리 우선순위 
print(3+12 > 7+3)