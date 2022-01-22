# Chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lamda)
# 함수의 중요성 -> 코드의 재사용성 / 코드의 안정성

# 함수 정의 방법
# def function_name(parameter):
#    <code>

# 예1
def first_func(w): 
    print("Hello,", w)
    
word = "Goodboy" # parameter

first_func(word)

# 예2
def return_func(w): 
    value = "Hello, " + str(w)
    return value
x = return_func("Goodboy2")
print(x)

# 예3(다중변환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) # 튜플로 팩킹

q = func_mul2(20)
print(type(q), q, list(q)) # 리스트로 형변환

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3] # 리스트로 팩킹

p = func_mul2(30)
print(type(p), p, set(q)) # set으로 형변환

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1, 'v2':y2, 'v3':y3} # 딕셔너리로 팩킹

d = func_mul3(30)
print(type(d), d, d.get('v2'), d.items(), d.keys()) # 딕셔너리로 출력 / get -> 지정한 key의 값을 출력 / items -> key와 value 값 출력 / keys -> 키 값만 출력

# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args): # 매개변수 명 자유 / args -> *가 있음 튜플 형태의 0번 index로 인식한다. / *가 없음 하나의 문자형으로 인식하여, 한글자 한글자 출력한다.
    for i, v in enumerate(args):
        print ('Result : {}'.format(i), v)
    print('-----') # 구분선
    
args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# 하나의 튜플 형태로 인식할 때, args 앞에 *을 쓴다.

# **kwargs(언팩킹)
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')

# 전체 혼합
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40) # 10, 20 -> arg_1, arg_2에 할당 / 'Lee', 'Kim', 'Park', 'Cho' -> *args에 할당 / age1=20, age2=30, age3=40 -> **kwargs

# 중첩 함수
def nested_func(num): # 100 할당
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
# 실행불가
# func_in_func(1000) 부모 함수를 호출하지 않고는, 안에 중첩되 있는 자식 함수는 정의되지않는다.

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#     return x * y

# lambda x, y: x * y

# 일반적함수 -> 변수
def mul_func(x, y):
    return x * y 

print(mul_func(10, 50)) # 10 * 50

mul_func_var = mul_func # 변수에 할당
print(mul_func_var(20, 50)) # 20 * 50

# 람다 함수 -> 할당
lambda_mul_func = lambda x, y: x * y # lambda는 익명 함수이기때문에, 변수에 담아서 사용해야한다.
print(lambda_mul_func(50, 50)) # 50 * 50

def func_final(x, y, func):
    print(x * y * func(100, 100)) # 10 * 20 * 10000

func_final(10, 20, lambda x, y:x * y) # 람다를 쓰든, 이미 변수에 할당해놓은 함수를 쓰든, 자주 쓰는 함수를 람다로 정의 해놔도 3개 다 출력한다.