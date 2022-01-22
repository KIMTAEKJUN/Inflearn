# chapter06-2
# 파이썬 모듈
# Module -> 함수, 변수, 클래스 등 파이썬 구성 요소들을 모아놓은 파일

def add(x, y): # 덧셈
    return x + y

def subtract(x, y): # 뺄셈
    return x - y

def multiply(x, y): # 곱셈
    return x * y

def divide(x, y): # 나누기
    return x / y

def power(x, y): # 제곱
    return x ** y 

# print('-' * 15)
# print('called! inner!')
# print(add(5, 5)) # 5 + 5 = 10
# print(subtract(15, 5)) # 15 - 5 = 10
# print(multiply(5, 5)) # 5 * 5 = 25
# print(divide(10, 2)) # 10 / 2 = 5.0
# print(power(5, 3)) # 5 * 5 * 5 = 125
# print('-' * 15)

# __name__ 사용
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__!')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print('-' * 15)