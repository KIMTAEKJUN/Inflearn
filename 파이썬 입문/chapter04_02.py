# chapter04-2
# 파이썬 반복문
# for문 실습

# 코딩의 핵심
# for in <collection>
#    <Loop body>

for v1 in range(10): # 0 ~ 9 / stop
    print('v1 is :', v1)

print()

for v2 in range(1, 11): # 1 ~ 10 / start, stop
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2): # 1, 3, 5, 7, 9 / start, stop, step
    print('v3 is :', v3)

# 1 ~ 1000까지의 합
sum1 = 0

for v in range(1, 1001): # 1 ~ 1000
    sum1 += v # sum1 = sum1 + v / sum1에다가 1씩 누적시킨다.
    
print('1 ~ 1000의 합 :', sum1) # 총 값이 나온다.
print('1 ~ 1000 4의 배수의 합 :', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕서녀리) 사용가능
# Iterables 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are :', name) # 리스트 값도 다 출력

# 예2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Currnet number :", n) # 리스트 값도 다 출력

# 예3
word = 'Beautiful'

for s in word:
    print('word :', s) # 문자열 한글자 한글자 반복해서 출력

# 예4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print('key :', key) # key를 출력한다.

for v in my_info.values(): # values를 써서 value 값만 출력한다.
    print('value :', v)

# 예5
name = 'FineAppLE'

for n in name:
    if n.isupper(): # 대문자라면 그냥 n을 출력
        print(n)
    else: # 소문자인 경우 n을 대문자로 바꿔 출력
        print(n.upper())

# break / for문 탈출
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34: 
        print('Found : 34!')
        break # 34을 찾게되면 break로 인해 멈추게되고, 뒤에 코드는 실행시키지않는다.
    else:
        print('Not Found :', num)

# continue / 다시 조건을 검사
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool: # 자료형을 대조할 때 is 사용
        continue # boolean을 찾으면 위 for문으로 돌아가서 코드를 실행시킨다.
    print("Current type :", v, type(v))
    print("Multiply by 2", v * 3)

# for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print('Found : 24')
        break # 24를 찾으면 break로 인해 멈추게되고, 뒤에 코드는 실행시키지않는다.
else: # 24를 찾지못하면 실행
    print('Not Found : 24')

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='') # end를 줘서 더 깔끔하게 코드가 출력되도록 한다.
    print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2)) # reversed를 호출하여, id값이 나온다. 그러므로 형 변환을 해줘야한다.
print('List', list(reversed(name2))) # 리스트으로 형 변환을 해, 'Aceman'를 반대로 출력
print('Tuple', tuple(reversed(name2))) # 튜플으로 형 변환을 해, 'Aceman'를 반대로 출력
print('Set', set(reversed(name2))) # 순서없음 / 집합으로 형 변환을 해, 'Aceman'를 랜덤으로 출력
