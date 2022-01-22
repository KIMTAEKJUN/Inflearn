# Chapter06-1
# 파이썬 클래스
# Object Oriented Programming Language (OOP : 객체 지향 프로그래밍) -> 객체를 우선으로 생각해서 프로그래밍하는 것이다.
# Self -> 인스턴스화된 어느 대상 
# 인스턴스 메소드 -> self를 인자로 받는 것들 
# 인스턴스 변수 - > self를 붙이고 선언하는 변수들

# 클래스 and 인스턴스 차이 이해
# 클래스 -> 붕어빵 틀 / 인스턴스 -> 코드에서 사용하는 어떤 객체, 인스턴스는 어떻게보면 객체에 포함된다.

# 예1
class Dog: # Object 상속
    # 클래스 속성(클래스 변수)
    species = 'firstdog'

    # 초기화 / 인스턴스 속성, 파이썬의 기본 문법
    def __init__(self, name, age): # 파이썬에서 클래스 초기화할 때 반드시 한 번 호출되는 함수 __init__(self)
        self.name = name # 인스턴스 변수
        self.age = age # 인스턴스 변수

# 클래스 정보
print(Dog)

# 인스턴스 화
# 계속 하나의 틀을 가지고 변수로 할당시키고, 메모리에 올라가고, ID값을 갖는다. -> 설계도를 바탕으로 구현된 것을 인스턴스화 되었다 말한다.
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
# 네임스페이스 -> 객체를 인스턴스화 할 때 저장 된 공간
# 클래스 변수 -> 직접 접근 가능, 공유
# 인스턴스 변수 -> 객체마다 별도 존재
print('dog1', a.__dict__) # 위에서 할당시킨 값들을 출력시킨다.
print('dog2', b.__dict__) # 위에서 할당시킨 값들을 출력시킨다.

# 인스턴스 속성 확인
print("{} is {} and {} is {}".format(a.name, a.age, b.name, b.age)) # 각 인스턴스 변수에 있는 속성값들을 출력

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species) # 클래스로도 접근 가능
print(a.species) # 인스턴스화 된 변수로도 접근 가능
print(b.species) # 이로써 하나의 값을 모두 공유하고있다는 걸 알 수 있다.

# 예2
# self의 이해
class SelfTest: # __init__ 없어도 파이썬이 내부적으로 실행해주기떄문에
    def func1(): # 클래스 메소드 / f의 대한 id값을 넘겼는데 func1에서 받지않으니, 예외가 발생한거다.
        print('Func1 called')
    def func2(self): # self는 인스턴스를 요구한다. / 클래스를 생선한 인스턴스화 시킨 변수가 self로 넘어간다.
        print(id(self))
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() 예외
f.func2()

SelfTest.func1() # 클래스로 직접 접근해서 호출
# SelfTest.func2() 예외 발생
SelfTest.func2(f) # 인스턴스화 된 변수를 넣어줘야 호출

# 예3
# 클래스 변수, 인스턴스 변수
class Warehouse: # 창고라는 클래스 선언
    # 클래스 변수 = 0
    stock_num = 0 # 재고, 모두 공유

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1 # 객체가 만들어질 때 1 증가

    def __del__(self):
        Warehouse.stock_num -= 1 # 소멸될 땐 1 감소

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50 / 직접 접근해서 수정하는 것은 좋지않다.
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('Before', Warehouse.__dict__) # stock_num이 공유하고 있던 2로 호출
print('>>>', user1.stock_num) # 2

del user1 # __del__ 호출
print('After', Warehouse.__dict__) # stock_num이 공유하던 2에서 1로 감소하여, 호출

# 예4
class Dog:
    species = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self): # 개의 행동을 메소드로 구현
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound): # 개의 짖는 행동을 메소드로 구현
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)

# 메소드 호출
print(c.info()) # c의 info에서 문자가 넘어오기때문에 print문로 찍어줘야한다.
print(d.info())

# 메소드 호출
print(c.speak('Wal Wal')) # self 넘겨줬지만, speak은 직접 지정해서 넘겨야됀다.
print(d.speak('Mung Mung'))