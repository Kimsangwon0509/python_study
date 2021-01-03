#파이썬 묘듈
# 재사용이 가능하게 공용으로 사용이 가능하게 
# 원하는 기능만 골라서 쓸수 있도록
#함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아 놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide (x, y):
    return x / y

def power(x, y):
    return x ** y

# 내 자신이 실행 될 때에는 메인이어서 실행된다.
if __name__ == "__main__":
    print('123')
# print('-' * 15)
# print('called! inner!')
# print(add(5,5))
# print(subtract(5,5))
# print(multiply(5,5))
# print(divide(5,5))
# print(power(5,5))
# print('-' * 15)