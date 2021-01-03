#모듈 사용 실습

import sys

print(sys)
print(sys.path)

# 모듈 경로 삽입 임시적으로 삽입 되는 것 
sys.path.append('C:/math')

print(sys.path)

#import chapter12_01

# 묘듈 사용
#print(test_modeul.power(10,3))

import chapter12_01

# __name__ 사용
 
