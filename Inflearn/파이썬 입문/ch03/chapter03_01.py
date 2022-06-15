# Chapter03-1
# 숫자형 사용법

# 숫자는 1에서 0으로 이루어진 정수가 있고, 3.1412 같은 실수가 있다. / 파이썬뿐만 아니라 모든 프로그래밍 언어에선 형변환을 잘 알고있어야됀다.
# 파이썬에서 지원하는 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""
# 시퀀스 -> 반복을 처리 가능, 어떤 순서가 있는걸 의미한다.

# 데이터 타입
str1 = "Python"
bool = False
str2 = 'Anaconda'
float_v = 10.0 # 10 == 10.0 
int_v = 7
list = [str1, str2]

# dict 타입에서의 "name"과 "version" 은 key라고 한다.
dict = {
    "name": "Machine Learning",
    "version": 2.0
}

tuple = (7, 8, 9)
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+ 
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) x ** y -> 2 ** 3 -> x에 y제곱을 의미한다.
"""

# 정수 선언
i = 77
i2 = -14

# Java 같은 언어에선 biginteger 같은걸로 값을 넣어야되는데, python은 마음 편히 집어 넣으면됀다.
big_int = 7777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 78192739871269586918276498172
big_int2 = 12309128095712859128591231251
f1 = 1.234
f2 = 3.939

# +
print(">>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# 서로 다른 형을 계산하면 자동으로 형변환이 이루어진다.

# *
print(">>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

# -
print(">>>>>-")
print("i1 - i2 : ", i1 - i2)
print("f1 - f2 : ", f1 - f2)
print("big_int1 - big_int2 : ", big_int1 - big_int2)

# %
print(">>>>>%")
print("i1 % i2 % ", i1 % i2)
print("f1 % f2 : ", f1 % f2)
print("big_int1 % big_int2 : ", big_int1 % big_int2)

# /
print(">>>>>/")
print("i1 / i2 : ", i1 / i2)
print("f1 / f2 : ", f1 / f2)
print("big_int1 / big_int2 : ", big_int1 / big_int2)

# //
print(">>>>>//")
print("i1 // i2 : ", i1 // i2)
print("f1 // f2 : ", f1 // f2)
print("big_int1 // big_int2 : ", big_int1 // big_int2)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 형 변환
print(float(b)) # 정수인 b를 실수로 바꿨다. / 6.0
print(int(c)) # 실수인 c를 정수로 바꿨다. / 7
print(int(d)) # 실수인 d를 정수로 바꿨다. / 12
print(int(True)) # True = 1, False = 0
print(float(False)) # float이기때문에 원랜 0인데 소수점을 붙여 0.0으로 출력됀다.
print(complex(3)) # 복소수로 반환
print(complex('3')) # 문자열로 3을 넣어도 위와 똑같이 출력됀다. / 문자형 -> 숫자형
print(complex(False))

print()

# 수치 연산 함수
print(abs(-7)) # 절대값이기때문에 7로 출력됀다.
x, y = divmod(100, 8)

print(x, y) # x = 몫, y = 나머지를 편안하게 자동으로 출력해준다.
print(pow(5, 3), 5 ** 3) # 5의 3제곱이기때문에 125가 출력됀다.

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi) # 원주율 출력
