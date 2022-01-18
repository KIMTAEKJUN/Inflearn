submit = int(input("입력 : "))
a = 0

for c in range(1, submit+1):
    if submit % c == 0:
        a += 1
        print("{} (은)는 {} 의 약수입니다.".format(c, submit))

if a == 2:
    print("{} (은)는 {} 과 {} 로만 나눌 수 있는 소수입니다.".format(submit, 1, c))