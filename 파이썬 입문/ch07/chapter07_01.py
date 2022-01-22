# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError
# 문법적으로 예외는 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리해야한다.
# 2. 로그는 반드시 남긴다. / 로그 -> 어떤 예외가 발생했었는지, 기록으로 남기는것, 어떠한 증거라고 볼 수있다.
# 3. 예외는 던져진다. / 다른 데로 처리를 위임할 수있다.
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('error) / 따옴표를 안붙였을 경우
# print('error')) / 닫는 괄호를 두개를 썼을 경우
# if True / :(콜론)을 안붙였을 경우 예외 발생
#     pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c) / 선언된 변수 a, b를 출력하지않고 위에서와 선언되지않은 변수 c를 출력하려하니 예외 발생

# ZeroDivisionError
# print(100 / 0) / 100을 0으로 나눌 수 없으니 ZeroDivisionError 예외 발생

# IndexError
# x = [50, 70, 90]
# print(x[1]) / 70
# print(x[4]) / 4번째 인덱스는 없기때문에 예외 발생
# print(x.pop()) / 정상 출력 / 50
# print(x.pop()) / 정상 출력 / 70
# print(x.pop()) / 정상 출력 / 90
# print(x.pop()) / 3번째 인덱스는 없기때문에 예외 발생

# KeyError
# dic = {
#     'name': 'Lee', / 'key': 'value'
#     'Age': 41,
#     'City': 'Busan'
# }
# print(dic['hobby']) / hobby를 가지고 있는 키가 존재하지않기때문에
# print(dic.get('hobby')) / get Method를 쓰는게 좀 더 안전하고 좋다. / 찾는 key가 없으면 None을 가져오기때문에

# 예외 없는 것을 가정하고 프로그램 실행 -> 런타임 예외 발생 시 예외 처리 권장(EAFP란 문서에 적혀있다.)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2()) / time이란 모듈에 time2란 속성이 없기때문에 예외 발생

# ValueError : 어떤 자료구조 안에서 및 시퀸스형 자료 안에서 데이터를 참조하려하는데 데이터가 존재하지않을때 예외
# x = [10, 50, 90]
# x.remove(50) / remove를 이용해 50이란 값을 지웠다
# print(x) / [10, 90]
# x.remove(200) / remove를 이용해 200이란 값을 지우라했지만, x 안에 200이란 값이 들어있지않기때문에 예외 발생

# FileNotFoundError
# f = open('test.txt') / test.txt란 텍스트 파일을 가져오라 했는데 파일을 찾을 수 없기때문에 예외 발생

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2] / list
# y = (1, 2) / tuple
# z = 'test' / 문자열

# print(x + y) / list와 tuple은 결합이 불가능하기때문에 에외 발생
# print(x + z) / list와 문자열은 결합이 불가능하기때문에 예외 발생
# print(y + z) / Tuple과 문자열은 결합이 불가능하기때문에 예외 발생

# print(x + list(y)) / 꼭 이런식으로 형변환을 해서 처리해야한다.
# print(x + list(z)) / 위와 동일

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행

name = ['Kim', 'Lee', 'Park']

# 예1
# try: try문 아래에 예외가 발생 할 가능성이 있는 코드들을 써서 실행.
#     z = 'Kim' / Kim이 있는지 찾는다.
#     x = name.index(z)  Kim은 0번째 인덱스에 있기때문에 0 출력
#     print('{} Found it! {} in name'.format(z, x + 1)) 
# except ValueError(): / ValueError가 나타난다면 실행
#     print('Not Found it! - Occurred ValueError!')
# else: / 에러가 발생하지않는다면 else 실행
#     print('OK Else!')

print()

# 예2
# try:
#     z = 'Cho' / 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1)) 
# except Exception: / Exception -> 모든 에러 예외를 Exception 하나로 다 잡는다. / 어떤 예외가 발생할지는 예측이 불가능하기때문에 포괄적으로 쓰기도한다.
#     print('Not Found it! - Occurred ValueError!')
# else:
#     print('OK Else!')

print()

# 예3
# try:
#     z = 'Cho' # 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1)) 
# except Exception as e: # elias로 e라는 별명을 선언해주고, 선언한다음 print하면 에러내용이 출력된다.
#     print(e)
#     print('Not Found it! - Occurred ValueError!')
# else:
#     print('OK Else!')
# finally: # finally는 예외가 발생했어도, 무조건 한번은 실행한다.
#     print('Ok! Finally')

# 예4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'Park'
    if a == 'Kim':
        print('Ok Pass!')
    else: # Kim이 아니면 무조건 예외를 발생시킨다.
        raise ValueError # raise 키워드로 직접 ValueError로 에러를 발생시켰다.
except ValueError(): # except로 ValueError를 직접 잡아서 처리 함.
    print('Occurred Exception!')
else:
    print('Ok Else!')