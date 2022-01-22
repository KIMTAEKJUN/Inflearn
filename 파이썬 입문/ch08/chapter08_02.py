# Chapter08-2
# 파이썬 외장(External)함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예1
import sys
print(sys.argv)

# 예2(강제 종료)
# sys.exit()

# 예3(파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 읽기, 쓰기
import pickle

# 예4(쓰기)
f = open('text.obj', 'wb') # write(쓰다), binary
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj, f) # pickle.dump를 이용해서 obj 쓸거고, 파일을 연결한 커넥션한 open 함수는 f 다
f.close() # 꼭 close를 이용해 닫아야한다, 언젠간 에러가 날 수있기때문에

# 예5(읽기)
f = open('text.obj', 'rb') # read(읽다), binary
data = pickle.load(f)
print(data, type(data)) # 타입이 딕셔너리인걸 알 수 있다.
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어있을 때), rename

# 예6
import os
print(os.environ)

# 예7(현재 경로)
print(os.getcwd()) # 현재 있는 경로 출력

# time : 시간 관련 처리
import time

# 예8
print(time.time())

# 예9(형태 변환)
print(time.localtime(time.time()))

# 예10(간단 표현)
print(time.ctime())

# 예11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) # Year, Month, Day | Hour, Min, Second

# 예12(시간 간격 발생)
# for i in range(5): / 0 ~ 4
#     print(i)
#     time.sleep(1) / 1초마다 쉬고 반복문 실행

# 예13
# random : 난수 리턴
import random
print(random.random()) # 0 ~ 1 사이의 값이 계속 랜덤 출력

# 예14
print(random.randint(1, 45)) # 1 ~ 45 사이의 값을 정수형으로 랜덤 출력
print(random.randrange(1, 45)) # 1 ~ 44 사이의 값을 정수형으로 랜덤 출력

# 예15(섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d) # d의 값들을 랜덤으로 섞는다.
print(d)

# 예16(무작위 선택)
c = random.choice(d) # d의 값 중 아무거나 초이스해서 출력한다.
print(c)


# Webbrowser
import webbrowser

webbrowser.open("http://www.naver.com/") # 브라우저가 실행되면서, 작성한 주소로 방문한다.

webbrowser.open_new("http://www.naver.com/") # 새 창으로 연다. / 기존에 탭이 있으면, 탭을 추가해서 열린다.