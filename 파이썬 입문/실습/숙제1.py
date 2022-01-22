submit = int(input("입력 : "))

for c in range(1, submit+1):
    if submit % c == 0:
        print("{} (은)는 {} 의 약수입니다.".format(c, submit))

# submit = int(input()) 변수를 만들어서 입력 받을 수 있게 만들어준다.
# 입력 : 9
# 1부터 시작, + 1
# submit % c == 0 일때 출력해주고, 나머지는 출력하지않는다.
# 1, 3, 9들이 9의 약수이다.