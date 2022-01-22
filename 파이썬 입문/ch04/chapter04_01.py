# Chapter04-1
# 파이썬 제어문
# IF문 실습
# IF문 -> "조건문" 참과 거짓을 판단하는 문장

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1, 2, 3], (1, 2, 3), {1, 2, 3} . . . / 데이터가 들어있는 것들은 모두 참(True) 취급
print(type(False)) # 0, "", [], (), {} . . . / 비어있는 것들은 모두 거짓(False) 취급

# 예1
if True:
    print('Good') # 문자열이기 때문에 참(True)

if False:
    print('Bad') # 빈 문자열이 아니기때문 출력 X

# 예2
if True:
    print('Bad')
else: # 위에서 True가 아니면 밑에껄 출력한다.
    print('Good!')

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양 변이 같을 경우 참
print(x == y)

# 양 변이 다를 경우 참
print(x != y)

# 왼쪽이 클 경우 참
print(x > y)

# 왼쪽이 크거나 같을 경우 참
print(x >= y)

# 오른쪽이 크거나 클 경우 참
print(x < y)

# 오른쪽이 크거나 같을 경우 참
print(x <= y)

# 예3
city = ""

if city:
    print("You are in : ", city)
else: # city 안에 빈 문자열이기때문에 False이다. 그러므로 Plz enter your city 출력
    print("Plz enter your city")

# 예4
city = "Seoul"

if city:
    print("You are in : ", city)
else: # city 안에 문자열이기때문에 True 이다. 그러므로 You are in : Seoul 출력
    print("Plz enter your city")

# 논리 연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and :', a > b and b > c) # a > b > c / and 는 모든 조건이 만족해야 출력 / 참(True)
print('or :', a > b or b > c) # or 은 한 쪽만 조건이 만족해도 출력 / 참(True)
print('not :', not a > b) # not 은 반대로 출력 / 참(True) -> 거짓(False), 거짓(False) -> 참(True) / 거짓(False)
print('not :', not b > c) # 거짓(False) 
print('not :', not True) # 거짓(False)
print('not :', not False) # 참(True)

# 산술, 관계, 논리 우선순위
# 산술 -> 관계 -> 논리
print('e1 :', 3 + 12 > 7 + 3) # 15 > 10, 비교해보면 왼쪽이 더 크기때문에 참(True) 출력
print('e2 :', 5 + 10 * 3 > 7 + 3 * 20) # 35 > 67, 비교해보면 오른쪽이 더 크기때문에 거짓(False) 출력
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10) # 참(True)
print('e4 :', 5 + 10 > 0 and not 7 + 3 == 10) # 거짓(False)

score1 = 90
score2 = 'A'

# 예4
# 복수의 조건이 모두 참일 경우에 출력
if score1 >= 90 and score2 == 'A': # and이니 양쪽 조건이 똑같이 참(True)이면 출력
    print('Pass')
else:
    print('Fail')

# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platium'

if id1 == 'vip' or id2 == 'admin': # or이니 양쪽 조건중 한 조건만 참(True)이면 출력
    print('관리자 입장')

if id2 == 'admin' and grade == 'platium': # 양쪽 조건 다 참(True)이니 출력
    print('최상위 관리자')

# 예6
# 다중 조건문

num = 90

if num >= 90: # num이 90이상이면
    print('Grade : A') # Grade : A 출력
elif num >= 80: # num이 80이상이면
    print('Grade : B') # Grade : B 출력
elif num >= 70: # num이 70이상이면
    print('Grade : C') # Grade : C 출력
else: # num이 70이하면
    print('과락')  # 과락 출력

# 예7
# 중첩 조건문
grade = 'A'
total = 95

if grade == 'A': # 무슨 시험이든 A를 받아야 장학금을 받을 수 있음.
    if total >= 90: # total이 90이상이면 장학금 100%를 지급
        print('장학금 100%') # 장학금 100% 출력
    elif total >= 80: # total이 80이상이면 장학금 80%를 지급
        print('장학금 80%') # 장학금 80% 출력
    else: # A를 받은 사람이면 모두 장학금 50%를 지급함.
        print('장학금 50%') # 장학금 50% 출력
else: # A를 받지 못한 사람은 total이 높아도 장학금을 받지 못함.
    print('장학금 없음') # 장학금 없음 출력

# in, not in
q = [10, 20, 30] # 리스트 선언
w = {70, 80, 90, 100} # 집합 선언
e = {"name": "Lee", "city": "Seoul", "grade": "A"} # 딕셔너리 선언
r = (10, 12, 14) # 튜플 선언

print(15 in q) # q에 있는 리스트 안에 15가 없으니 False 출력
print(90 in w) # w에 있는 집합 안에 90이 있으니 True 출력
print(12 not in r) # r에 있는 튜플 안에 12가 있어서 True지만 not을 붙였기 때문에 False 출력
print("name" in e) # e에 있는 딕셔너리 안에 name이란 키가 있기 때문에 True 출력
print("Seoul" in e.values()) # e에 있는 딕셔너리 안에 values()를 써서 키는 버리고 값("Seoul")만 출력하기 때문에 True 출력