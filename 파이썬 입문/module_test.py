# 모듈 사용 실습
import sys

print(sys.path) # 이 경로 안에서 만들어놓은 모듈을 패키지를 검색한다.

print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append("/Users/math") 코드 상에서만 append 됌 / 영구적으로 할라면 파이썬 패스에 영구적으로 등록해야 됌

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10, 3))

# import chapter06_02

# print(chapter06_02.add(10, 10000000)) # 10 + 10000000