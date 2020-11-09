#다양한 변수 선언법
# 변수 할당 설명
# Object Identity
# 변수 네이밍 규칙
# 예약어

#기본 선언
n = 700 

#출력
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var = "Change value"
print(var)
print(type(var))

#Object References
# 변수의 값이 할당 상태 일때
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

#예1)
print(300) # 300은 변수로 할당 안했음
print(int(300))

# 예2)
# n -> 777
n = 777
print(n, type(n))

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method  를 선언할때
# Pascal Case : NumberOfCollegeGraduates -> 클래스를 선언할때
# Snake Case : number_oof_college_graduates -> 변수를 선언할대

student_grade = 3
studentGrade = 3

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age = 7 
age_ = 8
_AGE = 9
