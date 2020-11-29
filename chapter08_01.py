#While 구문
#for문과는 조금 다름 
#if, for, while을 흐름 제어문으로 씀 . 

# while <expression>  표현식이 들어감
#   <statement(s)>
# 조건에 만족할떄 까지 반복을 한다. 

# 예제1

n = 5
while n > 0:
    print(n)
    n = n - 1

# 예제 2
a = ['abc', 'bar', 'bax']

while a:
    print(a.pop())

a = ['abc', 'bar', 'bax']
while a:
    print(a.pop(-1))

# 예제 3
# break , continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('end')


# 예제 4
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('end')

#예제 5

i = 1
while i <= 10:
    print(i)
    if i == 6 :
        break
    i += 1

#예제 6 while else
print('>>>>>>>>>>>>>>>>>')
n = 10
while n > 0 : 
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('end')

# 예제 7
a = ['foo', 'bar', 'baz', 'quz']
s = 'qussz'
i = 0
print('>>>>>>>>>>>>>>>>>>>')
while i < len(a):
    if a[i] == s:
        break
    i += 1
    print(i)
else:
    print(s,'not found')

#while True 는 무한 반복이므로 사용 X
