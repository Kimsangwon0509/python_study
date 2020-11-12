#형 변환 실습

f = 3 
b = 6
c = .7
d = 12.6
print(type(f))
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1 ,False : 0
print(float(False))
print(complex(3)) #complex는 복소수 
print(complex('3')) #문자형을 숫자형으로 바꾸고 실행 
print(complex(False))

#수치 연산 함수 
print(abs(-7))
x, y  = divmod(100, 8)
print(x, y)
print(pow(5,3), 5**3)

#외부 묘듈
import math

print(math.ceil(5.1))
print(math.pi)
