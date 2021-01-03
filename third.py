#숫자형 사용법
# 파이썬 모든 자료형
#데이터 타입 선언
#연산자 활용
#형 변환
#외부 모듈 사용

#Chapter 03-1
#숫자형

#파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합 
dict : 사전
"""

#데이터 타입
str1 = "Python"
bool = True
str2 = '김상원'
float = 10.0 # 10 == 10.0 컴퓨터는 같지 않다고 인식 
int = 7
list = [str1, str2]
print(list)
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)
set ={3, 5, 7}

#숫자형 
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x의 y 제곱을 계산  
"""


#정수 선언
i = 77 
i2 = -14
big_int = 777777777777777777777777777777777999999999999999999999999999999999

#정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f1 = 3.1231 
f2 = -3.9
f3 = 3 / 9

#실수 출력
print(f)
print(f1)
print(f2)
print(f3)

#연산 실습
i1 = 39
i2 = 399
big_int1 = 983475070234857023745908708237405987305
big_int2 = 32404327523456983204572358976234958692345
f1 =1.123
f2 = 5.326