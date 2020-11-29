#for 문
#for in <collection>
#   <Loop body>

for v1 in range(10): # 0 ~ 9
    print(v1)
print('>>>>>>>>>>>>>>')
for v2 in range(1, 2):
    print(v2)
print('>>>>>>>>>>>>>>')
for v3 in range(1, 11, 2):
    print(v3)



sum1 = 0
for v4 in range(1,1001):
    sum1 += v4

print(sum1)

#Iterables 자료형 반복은 모두 for 문에서 사용이 가능하다
# 문자열, 리스트, 튜플 , 집합, 사전(딕셔너리
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip이 사용 가능한 함수들

#예제1
names = ['Kim', 'Park', 'Cho', 'Lee','Yoo']

for name in names:
    print(name)

#예제 2

lotto_numbers = [11,12,32,56,43]

for n in lotto_numbers:
    print(n)

#예제 3

word = "abcdef"

for w in word:
    print(w)

#예제 4

info = {
    'name':'123',
    'key':1,
    'index':True
}

for k in info:
    print(k)

for k in info.values():
    print(k)

#example 5
name ='asdfQfwdsFREW'

for n in name:
    if n.isupper():
        print(n)
    elif n.upper():
        print(n.upper)

#break ///for 문을 탈줄 할때 씀
number = [1,2,3,4,5,6,7,678,8,3,45,45,6,7,3,5,4,457]

for num in number:
    if num == 4:
        print('found',num)
        break
    else:
        print('not found', num)

#continue 어떤 조건안에서 만나면 다시 조건을 검사하는 부분으로 이동

lt = ['1',"232313",True,complex(4),5.5,False,2]

for v in lt:
    if type(v) == bool:
        continue
    print(v)
#boolean형만 제외하고 나옴 컨디뉴로 통과시킴.


#for - else
numbers1 = [1,2,3,4,5,6,7,678,8,3,45,45,6,7,3,5,4,457]

for num in numbers1:
    if num == 3:
        print('found',num)
        break
else:
    print('not found')

#포문이 중단되지 않은경우에는 else문이 된다. break나 return을 만나면 else가 반환되지 않음.


#구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i * j), end='')  #4자리의 정수형으로 , 줄바꿈이 되지 않게 end
    print() #줄바꿈 처리 




# 변환 예제
name = 'Aceman'

print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
print(set(reversed(name))) #set집합은 순서가 없다. 중복은 허용이 안됨. 