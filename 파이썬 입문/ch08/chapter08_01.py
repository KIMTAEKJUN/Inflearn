# Chapter08-1
# 파이썬 내장(Built-in)함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs()

print(abs(-3))

# all, any : iterable 요소 검사(참, 거짓)
print(all([1, 2, 3])) # all() -> and / 모두 만족
print(any([1, 2, 0])) # any() -> or / 하나라도

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67)) # 아스키코드 문자로 바꿔 출력
print(ord('C')) # 문자를 아스키코드로 바꿔 출력

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name) # i -> 인덱스 번호, name -> value값을 가져옴 / 0 abc / 1 bcd / 2 efg

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2 # 2보다 크지않으면 filter로 인해서 걸리진다.

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6]))) # 람다식으로도 쓸 수있다.

# id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

# len : 요소의 길이 변환
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# max, min : 최댓값, 최솟값
print(max([1, 2, 3]))
print(max('python study'))
print(min([1, 2, 3]))
print(min('pythonstudy')) # 공백을 포함시키면, 공백을 가장 작게 인식하기때문에 붙여서 실행시켜야한다. A B C D E F G H I J K L N M O P Q R S T U V W X Y Z

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 6]))) # map은 함수를 통과시켜서 나오는 값들을 다시 한번 재결합해서 리스트로 형변환을 했다.
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6]))) # 람다식으로도 쓸 수있다.

# pow : 제곱값을 반환
print(pow(2, 10)) # 2의 10승 = 1024

# range : 반복가능한 객체(Iterable)를 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

# round : 반올림
print(round(6.5781, 2)) # 소수점 둘째자리에서 반올림해라
print(round(5.6))

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환
# list, tuple, set, dict -> 파이썬의 핵심 데이터 타입
print(sorted([6, 7, 4, 3, 2, 1])) # 오름차순으로 정렬

a = sorted([6, 7, 4, 3, 2, 1])
print(a)
print(sorted(['p', 'y', 't', 'h', 'o', 'n'])) # ABCDEFGHIJKLMNOPQR -> 알파벳 오름차순 순서대로 정렬

# sum : 반복가능한 객체(Iterable) 합 변환
print(sum([6, 7, 8, 9, 10])) # 6 ~ 10 합
print(sum(range(1, 101))) # 1 ~ 100 합

# type : 자료형 확인
print(type(3)) # 정수형인지 확인
print(type({})) # 딕셔너리인지 확인
print(type(())) # 튜플인지 확인
print(type([])) # 리스트인지 확인

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 변환
print(list(zip([10, 20, 30], [40, 50, 60]))) # 서로 튜플로 묶는다, 짝이 있는거끼리만 묶는다, 짝이 없음 묶지않는다.
print(type(list(zip([10, 20, 30], [40, 50, 777]))[0])) 