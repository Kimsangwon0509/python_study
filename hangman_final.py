# 행맨 미니 게임 제작

import time
import csv
import random
# 사운드 처리
import winsound
# 처음 인사 하기
name = input("이름을 입력하세요 : ")

print('Hi, ' + name, "게임을 시작할 시간입니다." )

print()

time.sleep(1)

print('로딩중......')

print()

time.sleep(0.5)

# CSV의 단어의 리스트를 선언 (CSV 파일은 추후에 추가)
words = []

# 문제 CSV 파일 로드
with open('./src/file.csv','r') as file:
    reader = csv.reader(file)
    # 헤더 스킵
    next(reader)

    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

print(q)
# 정답

word = "secret"

# 추측 단어
guesses =''

# 기회
turns = 10

# 핵심 while loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    #실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어를 반복
    for char in word:
        # 정답 단어 내에 추측 단어가 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end='')
        else:
            # 틀린 경우 대시로 처리
            print("_", end=' ')
            failed += 1
    # 단어 추측이 성공 한 경우 
    if failed == 0:
        print()
        print()
        # 성공 사운드 
        winsound.PlaySound('./sound.good.wav',winsound.SND_FILENAME)
        print('행맨 종료')
        break

    # 추측 단어 문자 단위 입력
    print()
    print('힌트는 {}'.format(q[1].strip()))
    guess = input("글자: ")

    # 단어 더하기 
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        #기회 갯수를 감소 
        turns -= 1
        #오류 메세지
        print('틀림')
        print('남은 기회 ',turns , ' 남음')

        if turns == 0:
            #실패 메세지
            winsound.PlaySound('./sound.bads.wav',winsound.SND_FILENAME)
            print('모든 턴을 소진')