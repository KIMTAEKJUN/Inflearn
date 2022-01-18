# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서없음, 중복불가)

# 선언
a = set() # 빈집합
b = set([1, 2, 3, 4, 4, 4, 4]) # 리스트 형태로 선언
c = set([1, 4, 5, 6]) # 이하 동문
d = set([1, 2, 'Pen', 'Cap', 'Plate']) # 서로 다른 자료형을 선언할 수 있음
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # key가 없이 값만 선언하면 집합이다.
f = {42, 'foo', (1, 2, 3), 3.14159} # 튜플도 선언할 수 있고, 실수형도 가능

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환 ( set -> tuple )
t = tuple(b)
print('t - ', type(t))
print('t - ', t[0], t[1:3]) # 인덱스 0번째 값 출력, 인덱스 2~3번째 값 출력 / 1 (2, 3)

# 리스트 변환 ( set -> list )
l = list(c) # c를 리스트로 변환
l2 = list(e) # e를 리스트로 변환
print('l - ', l) # [1, 4, 5, 6]
print('l2 - ', l2) # ['foo', 'bar', 'qux', 'baz']

# 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print('e - ', len(e))
print('f - ', len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print('s1 & s2', s1 & s2) # s1과 s2의 교집합을 출력시킨다. / {4, 5, 6}
print('s1 & s2', s1.intersection(s2)) # 이하 동문

print('s1 | s2', s1 | s2) # s1과 s2의 합칩합을 출력시킨다. / {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 | s2', s1.union(s2)) # 이하 동문

print('s1 - s2', s1 - s2) # s1과 s2의 차집합을 출력시킨다. / {1, 2, 3}
print('s1 - s2', s1.difference(s2)) # 이하 동문

# 중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2)) # s1과 s2가 교집합을 가지고있는지 출력시킨다. / False -> 있음, True -> 없음 / False

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # s1이 s2의 부분집합이냐 물어본다. / False 
print('superset : ', s1.issuperset(s2)) # s1이 s2를 포함하고 있는지 물어본다. / False

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5) # add 메소드를 이용해서 5를 추가했다. / {1, 2, 3, 4, 5}
print('s1 - ', s1)

s1.remove(2) # remove 메소드를 이용해서 2를 삭제했다. / {1, 3, 4, 5} / 없는 값을 삭제할려했을 때 에러가 뜬다. 
print('s1 - ', s1)

s1.discard(3) # discard 메소드를 이용해서 3을 삭제했다. / {1, 4, 5} / 없는 값을 삭제할려했을 때 에러가 뜨지않는다.
print('s1 - ', s1)

s1.clear() # clear 메소드를 이용해서 전체 다 삭제했다. / set() / 리스트도 clear로 전체 다 삭제 가능
print('s1 - ', s1)

a = [1, 2, 3]
a.clear()
print(a)