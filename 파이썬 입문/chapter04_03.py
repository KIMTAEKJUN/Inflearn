# Chapter04-3
# 파이썬 반복문
# while문 실습

# while <expr>:
#     <statement(s)>
# while문은 if문이랑 똑같다.
# while문은 조건에 만족할 때까지 계속 반복을 한다.

# 예1
n = 5

while n > 0: # 0이 될 때까지 반복한다.
    print(n)
    n -= 1 # n = n - 1

# 예2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop()) 

# 예3
# break, continue
n = 5

while n > 0:
    n -= 1
    if n == 2:
        break # 2가 걸리면 break으로 인해, if문을 빠져나가서 맨 밑에 출력문 실행
    print(n) # 4, 3, Loop End
print('Loop End')

# 예4
m = 5

while m > 0:
    m -= 1
    if m == 2:
        continue # 2가 걸리면 continue으로 인해, 건너뛰고 다시 위 while문 실행
    print(m) # 4, 3, 1, 0
print('Loop End')

# 예5
# if 중첩
i = 1

while i <= 10:
    print('i :', i)
    if i == 6:
        break
    i += 1 # i = i + 1

# 예6
# while - else 구문
n = 10

while n > 0: # 10 > 0
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

# 예7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s: 
        break
    i += 1
else:
    print(s, 'not found in list.')

# 무한반복
# while True:
#     print()

# 예8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())