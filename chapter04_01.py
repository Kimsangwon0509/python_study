# Chapter03- 4
#파이썬 튜플
#리스트와 비교하는게 중요
# 튜플 자료형(순서ㅇ, 중복ㅇ, 수정 x , 삭제 x) 리스트는 다 됨 . # 불변 

# 선언

a = ()
b = (1)
#원소가 하나일때는 콤마를 찍어야 튜플로 인식을 한다
c = (11, 12, 13, 14)

print(type(a), type(b))
d = (100, 10000, 'Ace', 'Base', 'Captine')
e = (100, 10000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print(d[1])
print(d[0] + d[1]+ d[1])
print(d[-1])
print(e[-1])
print(e[-1][1])
print(list(e[-1][1]))

print(d[0:3])
print(d[2:])
print(e[2][1:3])

#튜플 연산
print(c + d)
print(c * 3)

#튜플 함수
a = (5, 2, 1 ,3, 4)
print( a)
print(a.index(3))
print(a.count(2))

# 팩킹 & 언팩킹(Packing, and Unpacking)
t = ('foo', 'bar', 'baz', 'qux')  #묶은것 자체가 인덱싱 

print(t)
print(t[0])
print(t[-1])

#언팩킹
(x1, x2, x3, x4) = t
x1, x2, x3, x4 = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)