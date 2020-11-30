# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

#함수 정의 방법
#def funciton_name(parameter) : 
#    code

#예제 1
def first_func(w):
    print("Hello ", w)

word = "Goodboy" 

first_func(word)

#예제 2
def second_func(w):
    value = "hello " +str(w)
    return value

x = second_func('abc')
print(x)

#다중3 (다중반환)
def func_mul(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return (y1, y2, y3)

x,y,z =func_mul(5)
print(x,y,z)

q = func_mul(20)
print(q)

#리스트 반환 (다중반환)
def func_mul2(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return [y1, y2, y3]


#튜플 반환 (다중반환)
def func_mul3(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return (y1, y2, y3)

#딕셔너리 리턴
def func_mul4(x):
    y1 = x* 10
    y2 = x* 20
    y3 = x* 30
    return {'v1':y1, 'v2':y2, 'v3':y3}