#값 비교
#선언
a =[]
b = list()
c = [70, 78, 75, 76] #len 가능
d = [1000, 10000, "Ace", 'bear', ' 서로다른 자료형을 한 리스트 안에 담을수 있다.']
e = [1000, 10203023, ['asd', 'asfasf', 'qwqwewww']]
f = [21.42, 'foobar', 3, 4, False, 3.1234]

print(c == c[:3] + c[3:])

#Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

c[0] = 4
print(c)
c[1:2] = ['a', 'b', 'c']# 괄호를 2개 사용해야 아래와 결과가 같은 [['a', 'b', 'c']]
print(c)
c[1] = ['a', 'b', 'c']  #들어갈 위치는 같지만 결과는 다름 ...
print(c)
c[1:3] = []
print(c)

# 제거
# del
del c[2]
print(c) 

# 리스트 함수
a = [5,1,2,34,56]
print(a)
#끝에다가 데이터를 넣고 싶으면 마지막 끝에다가 데이터를 넣는다
a.append(10)
print(a)
a.sort() #오름차순 정렬
print(a)
a.reverse() #역순으로 정렬
print(a)
print(a[3])
print(a.index(3))
a.insert(2,7) #두번쨰 위치에 7을 넣기 