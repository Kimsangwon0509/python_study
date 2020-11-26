#딕셔너리 
# 범용적으로 가장 많이 사용
# 순서 x , 키 중복 허용 x , 수정 ㅇ , 삭제 ㅇ 

# 선언 
a = {'name':'kim','phone':'0103334444','birth':'870514'}
b = {0:'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Status' : True,
    'Grade' : 'A'
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True,
)

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)


#출력
print(a['name'])
print(a.get('name'))
#print(a['name1']) 속성으로 부르면 오류가 나도
print(a.get('name1')) # get으로 출력하면 None이 뜬다.없을경우를 대비해서 get으로 가져오는게 안전 프로그램의 흐름이 끊기지 않는다
print(b[0])
print(b.get(0))
print(f.get('City'))

#딕셔너리 추가
a['address'] = 'busan'
print(a)
a['address'] = 'seoul' #자동으로 찾아서 수정
a['rank'] = [1,2,3]
print(a)
print(len(a))#키의 길이를 잰다

#딕셔너리에서 지원하는 함수들 주로 반복문을 위한 함수 

#dict_keys, dict_value, dict_items : 반복문에서 사용 가능 
print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())

print(a.pop('name'))

print(a.popitem())
#키를 가지고 있는지를 조회할수 있다.
print('bitrh2' in a)
print('City' in d)

#수정
a['test'] = 'test_dict'
print(a)

a['address'] = '대전'
print(a)

a.update(birth='910904')
print(a)

temp = {'address' : 'Busan'}

a.update(temp)
print(a)