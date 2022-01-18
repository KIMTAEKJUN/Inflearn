submit = input("입력 : ")


if submit.islower():
    print("%s(ASCII : %d) => %s(ASCII : %d)"% (submit, ord(submit),submit.upper(),ord(submit.upper())))
elif submit.isupper():
    print("%s(ASCII : %d) => %s(ASCII : %d)"% (submit, ord(submit),submit.lower(),ord(submit.lower())))
else:
    print("%s (ASCII : %d)"% (submit, ord(submit.lower())))