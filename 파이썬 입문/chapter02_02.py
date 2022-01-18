# Chapter02-2
# 파이썬 완전 기초
# 다양한 변수 선언법
# 변수 -> 데이터를 저장하기 위해 프로그램에 의해 이름을 할당받은 메모리 공간 / 값을 저장할 때 사용하는 식별자

# 기본 선언
n = 700

# 출력
print(n)

# type 함수는 n에 할당 돼 있는 값에 자료형을 보여준다. 
print(type(n))

print()

# 동시 선언
x = y = z = 700
print(x, y, z)

print()

# 선언
var = 75

# 재선언 ( 다시 재할당 되게 함 )
var = 'Change Value'

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 설정
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

# m 재할당
m = 400

print(m, n)
print(type(m), type(n))
print()

# id( identity ) 확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case -> numberOfCollegeGraduates -> Method 선언 / 단어들의 첫 글자를 대문자로 만들어 변수 선언 하는 방법
# Pascal Case -> NumberOfCollegeGraduates -> Class 선언 / 단어들의 첫 글자를 소문자로 만들어 변수 선언 하는 방법
# Snake Case -> number_of_college_graduates -> 변수 선언 / 단어 사이에 언더 바를 붙여 변수 선언 하는 방법 / 제일 추천하는 변수 선언 방법

# 허용하는 변수 선언 법
# 1. 숫자나 특수문자로 시작하는 변수는 안됌. 
# 2. 특수 문자는 언더바(_) 만 허용
# 3. 공백을 포함할 수 없음.
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 7

# 예약어는 변수명으로 불가능
# 변수로 사용불가능한 예악어

"""
False   def if  raise
None    del import  return
True    elif    in  try
and  else    is  while
as	except	lambda	with
assert	finally	 nonlocal	yield
break	for	 not	
class	from	or	
continue	global	pass
"""

# 원하는 어떤 오브젝트를 만들 때 그거에 알맞는 네이밍( 변수이름 )을 지어주는게 좋다.