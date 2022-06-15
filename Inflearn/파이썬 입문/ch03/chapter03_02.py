# Chapter03-1
# 파이썬 문자형
# 문자열 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm boy

print("I'm boy") # 큰따옴표로 할 땐 그대로 출력되지만, 작은따옴표로 했을 땐 에러가 난다.
print('I\'m boy') # 역슬래시를 사용하면 뒤에 있는 특수 기호는 있는 그대로 표시가 됀다.

print('a \t b') # \t -> 탭만큼 띄어쓰기
print('a \n b') # \n -> 줄바꿈

print('a \"\" b') # 역슬래시 뒤에 있는 큰따옴표를 이스케이프 시켜서 두개 그대로 출력시킨다.

escape_str1 = "Do you have a \"retro games\"?" # 이스케이프 문자를 사용하여 큰따옴표 안에 큰따옴표를 오류없이 출력했다.
print(escape_str1)
escape_str2 = 'What\'s on TV?' # 이스케이프 문자를 사용하여 작음따옴표 안에 작음따옴표를 오류없이 출력했다.
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!" # Click과 Start 사이의 \t를 입력하여 탭만큼 띄어쓰기를 시켜줬다.
t_s2 = "New line \n Check!" # New line과 Check 사이의 \n을 입력하여 Check을 줄바꿈 시켜줬다.

print(t_s1)
print(t_s2)

print()

# Raw String 출력 / 역슬래시 있는 그대로 표시
raw_s1 = r'D:\tpython\test'

print(raw_s1)

print()

# 멀티라인 입력 / 역슬래시를 입력하고 밑에 변수들을 써야 에러가 안나고 출력됀다.
# 꼭 역슬래시 사용
multi_str = \
"""
String
Multi Line
Test
"""

print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3) # 곱하기 연산으로 하면 숫자에 맞게 반복돼서 출력됀다.
print(str_o1 + str_o2) # Python과 Apple을 합쳐 출력한다.
print('y' in str_o1) # Python이란 단어 안에 y가 있나요? 라고 물어봤기때문에 True이 출력됀다.
print('n' in str_o1) # 위와 똑같다.
print('P' not in str_o2) # Apple이란 단어 안에 P가 없나요? 라고 물어봤기때문에 True이 출력됀다.

# 문자열 형 변환
print(str(66), type(str(66))) # 숫자 66이 아니라 문자 66으로 인식하여 출력한다.
print(str(10.1)) # 위와 똑같다.
print(str(True), type(str(True)))

# 문자열 함수 ( upper, isalnum, startwith, count, endswith, isalpha . . .)
print("Capitalize: ", str_o1.capitalize()) # capitalize 함수는 첫번째 글자를 대문자로 바꿔준다.
print("endswith?:", str_o2.endswith("s")) # endswith 함수는 마지막 글자가 무엇인지 확인한다.
print("replace", str_o1.replace("thon", 'Good')) # replace 함수는 문자 안에 있는 부분을 찾아 바꾸고싶은 문자로 바꾼다.
print("sorted: ", sorted(str_o1)) # sorted 함수는 정렬에서 리스트 형태로 변환 해준다.
print("split: ", str_o4.split(' ')) # split 함수는 정의하는 기준으로 정의 기준으로 분리하여 리스트 형태로 변환해준다.

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i) # 한 글자 한 글자 가져와 문자를 출력한다.

# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3]) # 0~2 해당하는 글자를 출력한다. / 0 1 2 까지 출력 무조건 -1 / Nic 까지 출력
print(str_s1[5:]) # [5:10] / Python만 출력
print(str_s1[:len(str_s1)]) # str_s1[:10] / Nice Python 출력
print(str_s1[:len(str_s1)-1]) # str_s1[:9] / Nice Pytho 출력
print(str_s1[1:9:2]) # 1~8 을 출력하는데, 2칸씩 띄어서 출력한다. / iePt 출력
print(str_s1[-5:]) # 오른쪽부터 -5칸부터 출력한다. / ython 출력
print(str_s1[1:-2]) # -2 이전글자인 h까지 출력한다. / ice Pyth 출력
print(str_s1[::2]) # 처음부터 끝까지 2칸씩 띄어서 출력한다. / Nc yhn 출력
print(str_s1[::-1]) # 처음부터 끝까지 출력하는데 오른쪽부터 / nohtyP eciN 출력

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 알파벳 z에 해당하는 아스키 코드 숫자값이 122번이라 아스키 코드 숫자 122을 출력한다.
print(chr(122)) # 122번에 해당하는 아스키 코드를 알파벳 z로 출력한다..

