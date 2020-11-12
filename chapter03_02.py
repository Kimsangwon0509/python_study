#Chapter03-2
#파이썬 문자형
#문자형 중요

#문자열 생성
str1 ='I am Python'
str2 = "python"
str3 ="""How are you"""
str4 = '''Thank You!'''

print(len(str1))

# 빈 문자열
str1_t1 = ''
str2_t2 = ""
str3_t3 = str()

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))
print(type(str3_t3),len(str3_t3))

#이스케이프 문자 사용
# I'm boy

print("I'm boy")
print("I\'m boy")
print("I\tm boy") #탭
print("I\nm boy") #줄바꿈

# Raw String 
#역슬레쉬 자체를 신경을 안씀
raw_s1 = r'D:\python\test'
#경로를 가지고 파일을 복사 한다든지 할때 사용 .
print(raw_s1)

#멀티라인 입력
multi_str = """
String 
Multi Line
Test
문자열
멀티라인입력
테스트
"""

multi_str2 =\
"""
줄바꿈으로 시작하는
멀티라인을
입력하는 방법
하면
슬레시를 넣어서 이어간다.
"""


print(multi_str)
print(multi_str2)

#문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul! Deajeon! Busan! Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)  
print('z' in str_o1)
print('P' not in str_o2)

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True),type(str(True)))


#문자열 함수(uppe, isalnum, startswith, count, endswith,  .....)

print("Capitalize: ", str_o1.capitalize())
print("endswith?:", str_o2.endswith("s"))
print("endswith?:", str_o2.endswith("e"))
print("replace?:", str_o1.replace("thon", "Good"))
print("sorted:", sorted(str_o2))
print("split: ", str_o4.split('!'))

#반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__ 라는게 있다.

#출력
for i in im_str:
    print(i)