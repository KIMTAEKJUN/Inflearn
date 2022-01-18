# Chapter02-1
# 파이썬 완전완전 기초
# 다양한 print문 출력

# 모두 출력 됌 ( 작은따옴표와 큰 따옴표를 가장 많이 활용한다. )
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

# print문에 공백을 쓰면 줄바꿈이 됌.
print()

# separator 옵션 ( sep 자주 사용 됌 )
print('P', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')


print()

# end 옵션 ( end 옵션에 들어간 문자로 다음 print문을 이어 질 수 있다. )
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
import sys

# file=지정한 파일에 내용을 쓴다.
print('Learn Python', file=sys.stdout)

print()

# format 사용 ( d 정수(int), s 문자열(string), f 실수(float) ) -> 이 세 가지를 제일 많이 사용함. -> ex) d : 3, s : 'Python', f : 3.14512412
# format() -> format() 함수는 문자열이 가지고 있는 함수
print('%s %s' % ('one', 'two'))

# format 함수가 내부적으로 처리해주기 때문에 좀 더 유연하게 사용 가능
print('{} {}'.format('one', 'two'))

# 인덱스는 무조건 0번째부터임 전공하면서 맨날 들음 지겨워
print('{1} {0}'.format('one', 'two'))

print()

# %s 사용법 

# 숫자가 오면 자릿수를 의마한다.
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

# 음수가 왔을 땐 오른쪽부터 공백으로 채우고, 양수는 왼쪽부터 공백으로 채운다.
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

# 왼쪽에서 채워지던 여백이 사라지고 밑줄로 채워진다.
print('{:_>10}'.format('nice'))

# ^ 표시는 가운데 정렬이다.
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))

# 점을 붙여야 절삭을 한다. 
print(('%.5s' % ('Pythonstudy')))

# 공간은 10개가 있고, 왼쪽부터 5개의 글자만 출력 한 것이다.
print('{:10.5}'.format('Pythonstudy'))

print()

# %d 출력
print('%d %d' % (1,2))
print('{} {}'.format (1,2))

# 그냥 있는 값이 출력 됌
print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f 출력
print('%f' % (3.14123213124))
print('{:f}'.format(3.1412312412))

# 정수부는 한개이기때문에 0으로 채웠다.
print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))

# 문자열일 땐 format(익스프레션 표현식)을 쓸 땐 s를 생략해줘도 돼지만, 정수나 실수에선 생략하면 안됀다.
# 소수부, 정수부 잘 구분해야됌