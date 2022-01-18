submit = input("입력 : ")

for c in submit:
    if c.isupper():
        print("{} 는 대문자 입니다.".format(c))
    else:
        print("{} 는 소문자 입니다.".format(c))