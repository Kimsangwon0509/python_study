#값 비교
#선언
a =[]
b = list()
c = [70, 78, 75, 76] #len 가능
d = [1000, 10000, "Ace", 'bear', ' 서로다른 자료형을 한 리스트 안에 담을수 있다.']
e = [1000, 10203023, ['asd', 'asfasf', 'qwqwewww']]
f = [21.42, 'foobar', 3, 4, False, 3.1234]

print(c == c[:3] + c[3:])