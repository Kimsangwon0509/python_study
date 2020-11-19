#Chapter03-3
#파이썬 리스트
#자료구조에서 중요
#리스트 자료형(순서o, 중복ㅇ, 수정 ㅇ, 삭제 ㅇ)

#선언
a =[]
b = list()
c = [70, 78, 75, 76] #len 가능
d = [1000, 10000, "Ace", 'bear', ' 서로다른 자료형을 한 리스트 안에 담을수 있다.']
e = [1000, 10203023, ['asd', 'asfasf', 'qwqwewww']]
f = [21.42, 'foobar', 3, 4, False, 3.1234]

#인덱싱
print('>>>>>')
print('d - ', type(d), d )
print('d - ', d[0])
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1][1])

#슬라이싱
print('d - ', d[0:3])
print('d - ',d[2:])
print('e - ',e[-1][1:3])

# 리스트 연산
print('>>>>')
print(c + d)
print(c * 3)