# Chapter03-5
# 딕셔너리(Dictionary) 사용법
# 범용적으로 가장 많이 사용 ( JSON )
# 딕셔너리 자료형(순서없음, 키 중복불가, 수정가능, 삭제가능)

# 선언
a = {"name": 'Kim', "phone": '01033337777', "birth": '870514'} # 딕셔너리는 중괄호 사용 / Key와 Value 값으로 이루어져있다.
b = {0: 'Hello Python'} # 키는 숫자로도 선언이 가능하다.
c = {'arr': [1, 2, 3, 4]} # 키만 존재한다면 어떤 값이든 어떤 자료형이든 상관없다.

# 들여쓰기를 해서 일자로 쭉 쓰는거보다 보기 좋게 정리하는게 좋다. / 많이 이용함.
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}

# dict() 선언 방법은 잘 사용하지않음 / 진짜 쓰지마세요
e = dict([
    ('Name', 'NiceMan'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

# 따옴표, 괄호 필요없이 더 편한 선언 방법 / 많이 이용함
f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Stauts = True
)

print('a - ', type(a), a)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d) # d부터 f까진 똑같은 딕셔너리 형태를 나타내고있다.
print('a - ', type(e), e) # 선언 방법은 모두 다르지만 파이썬은 정확하게 똑같은 데이터를 받아 하나의 딕셔너리로 출력했다.
print('a - ', type(f), f)

# 출력
print('a - ', a['name']) # a의 들어있는 'name'의 Value 값을 가져와 출력했다.
print('a - ', a.get('name')) # 위와 같이 똑같이 출력한다.

# print('a - ', a['name1']) # a의 값에는 'name1'이란 key가 없어 키에러가 난다. / 키가 없는 경우엔 키에러가 난다.
# print('a - ', a.get('name1')) # 하지만 get 함수를 사용하게되면 오류가 뜨지않고 None을 출력한다. / 키가 없는 경우엔 None으로 처리, 그래서 더욱 더 안정적이게 개발 가능

print('b - ', b[0]) # b에 있는 0번키 값을 출력한다. / Hello Python
print('b - ', b.get(0)) # 위와 같이 똑같이 출력한다.

print('f - ', f.get('City')) # f에 있는 'City' 키의 지정된 값을 출력한다. / Seoul
print('f - ', f.get('Age')) # f에 있는 'Age' 키의 지정된 값을 출력한다.  / 33

# 딕셔너리 추가
a['address'] = 'seoul' # a 안에 'address' 라는 키를 추가하여 값을 넣었다. / {'name': 'Kim', 'phone': '01033337777', 'birth': '870514', 'address': 'seoul'}
print('a - ', a)

# a['name'] = 'Lee' # 추가를 했는데 키 이름이 똑같으면 기본 값을 추가한 값으로 수정됀다.
print('a - ', a)

a['rank'] = [1, 2, 3] # 리스트 값도 추가가 됀다.
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용가능한 딕셔너리에서 지원하는 함수들
print('a - ', a.keys()) # a에 있는 value 값을 제외시키고, key 값만 출력시킨다. / (['name', 'phone', 'birth', 'address', 'rank'])
print('b - ', b.keys()) # b에 있는 value 값을 제외시키고, key 값만 출력시킨다. / ([0])
print('c - ', c.keys()) # c에 있는 value 값을 제외시키고, key 값만 출력시킨다. / (['arr'])
print('d - ', d.keys()) # d에 있는 value 값을 제외시키고, key 값만 출력시킨다. / (['Name', 'City', 'Age', 'Grade', 'Status'])

print('a - ', list(a.keys())) # dict_keys 라는 자료형에서 완전 리스트형태로 형변환하여 출력시킨다. / ['name', 'phone', 'birth', 'address', 'rank']
print('b - ', list(b.keys() )) # 이하 동문 / [0]

print()

print('a - ', a.values()) # a에 있는 key 값을 제외시키고, value 값만 출력시킨다. / (['Kim', '01033337777', '870514', 'seoul', [1, 2, 3]])
print('b - ', b.values()) # b에 있는 key 값을 제외시키고, value 값만 출력시킨다. / (['Hello Python'])
print('c - ', c.values()) # c에 있는 key 값을 제외시키고, value 값만 출력시킨다. / ([[1, 2, 3, 4]])
print('d - ', d.values()) # d에 있는 key 값을 제외시키고, value 값만 출력시킨다. / (['Niceman', 'Seoul', 33, 'A', True])

print('a - ', list(a.values())) # dict_values 라는 자료형에서 완전 리스트형태로 형변환하여 출력시킨다. / ['Kim', '01033337777', '870514', 'seoul', [1, 2, 3]]
print('b - ', list(b.values())) # 이하 동문 / ['Hello Python']

print()

print('a - ', a.items()) # a에 있는 key와 value가 하나의 튜플 형태로 key와 value가 한쌍을 이루어 출력시킨다. / ([('name', 'Kim'), ('phone', '01033337777'), ('birth', '870514'), ('address', 'seoul'), ('rank', [1, 2, 3])])
print('b - ', b.items()) # b에 있는 key와 value가 하나의 튜플 형태로 key와 value가 한쌍을 이루어 출력시킨다. / ([(0, 'Hello Python')])
print('c - ', c.items()) # c에 있는 key와 value가 하나의 튜플 형태로 key와 value가 한쌍을 이루어 출력시킨다. / ([('arr', [1, 2, 3, 4])])
print('d - ', d.items()) # d에 있는 key와 value가 하나의 튜플 형태로 key와 value가 한쌍을 이루어 출력시킨다. / ([('Name', 'Niceman'), ('City', 'Seoul'), ('Age', 33), ('Grade', 'A'), ('Status', True)])

print('a - ', list(a.items())) # dict_items 라는 하나의 튜플 안에 있는 key와 value를 리스트 형태로 형변환하여 출력시킨다. / [('name', 'Kim'), ('phone', '01033337777'), ('birth', '870514'), ('address', 'seoul'), ('rank', [1, 2, 3])]
print('b - ', list(b.items())) # 이하 동문 / [(0, 'Hello Python')]

print('a - ', a.pop('name')) # pop 함수를 써서, 'name' 안 맨끝에 있는 value를 꺼낸 다음 삭제시킨다. / Kim
print('a - ', a) # {'phone': '01033337777', 'birth': '870514', 'address': 'seoul', 'rank': [1, 2, 3]}
print('c - ', c.pop('arr')) # pop 함수를 써서, 'arr' 안에 있는 value를 꺼낸 다음 삭제시킨다. / [1, 2, 3, 4]
print('c - ', c) # 빈 딕셔너리만 남는다. / {}

print()

print('f - ', f.popitem()) # popitem 함수를 써서, f 안에 있는 key와 value를 무작위로 꺼내 삭제시킨다. / ('Stauts', True) / 이제 LIFO 순서가 보장됩니다.
print('f - ', f) # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A'}
print('f - ', f.popitem()) # popitem 함수를 써서, f 안에 있는 key와 value를 무작위로 꺼내 삭제시킨다. / ('Grade', 'A')
print('f - ', f) # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33}

print()

print('a - ', 'birth' in a) # in 연산자는 a에 'birth' 라는 key가 있어? 라고 물어본다. / True
print('d - ', 'birth' in d) # in 연산자는 d에 'birth' 라는 key가 있어? 라고 물어본다. / False

# 수정 & 추가
a['test'] = 'test_dict' # 'test' 라는 key와 'test_dict' 라는 value를 추가 시킨다. / {'phone': '01033337777', 'birth': '870514', 'address': 'seoul', 'rank': [1, 2, 3], 'test': 'test_dict'}
print('a - ', a)

a['address'] = 'dj' # 기존에 있던 'address' 라는 key에 value를 'dj'라는 value로 수정 시킨다. / {'phone': '01033337777', 'birth': '870514', 'address': 'dj', 'rank': [1, 2, 3], 'test': 'test_dict'}
print('a - ', a)

a.update(birth='910904') # a 값의 'birth' 에 value 값을 '910904'로 수정시킨다. / {'phone': '01033337777', 'birth': '910904', 'address': 'dj', 'rank': [1, 2, 3], 'test': 'test_dict'}
print('a - ', a) 

temp = {'address': 'busan'} # temp 라는 변수에 'address' 라는 key와 'busan' 이라는 value를 지정했다.
a.update(temp) # 수정할 때 이렇게 명시적으로 사용가능 / {'phone': '01033337777', 'birth': '910904', 'address': 'busan', 'rank': [1, 2, 3], 'test': 'test_dict'}
print('a - ', a)