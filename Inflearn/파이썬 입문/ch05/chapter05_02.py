# chapter05-2
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입은 무조건 문자열(str)

# input() -> 명령 프롬포트에서 사용자로부터 데이터를 입력 받을 때 쓰는 함수

# 예1
# name = input("Enter Your Name : ")
# grade = input("Enter Your Grade : ")
# company = input("Enter Your Company name : ")

# print(name, grade, company)

# 예2
# number = input("Enter number : ")
# name = input("Enter name : ")

# print("Type of number :", type(number))
# print("Type of name :", type(name))

# 예3
# first_number = int(input("Enter number1 : "))
# second_number = int(input("Enter number2 : "))

# total = first_number + second_number
# print("first_number + second_number :", total)

# 숫자같은 경우는 주의해서 사용해라

# 예4
float_number = float(input("Enter a float number : ")) # 입력받은 다음엔 무조건 형 변환을 해서 사용하는게 핵심이다.
print("Input float : ", float_number)
print("Input type : ", type(float_number))

# 예5
print("Firstname - {0}, Lastname - {1}".format(input("Enter first name :"), input("Enter second name :"))) # 함수 안에서도 사용가능