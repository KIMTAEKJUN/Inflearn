list1 = ["가위", "바위", "보"]
Man1 = input("입력 : ")
Man2 = input("입력 : ")
Result = "님 입력잘못했어요~"

if Man1 == list1[0]:
    #b가 낸것에 따라 결과 설정
    if Man2 == list1[0]:
        Result = "Result : Draw"
    elif Man2 == list1[1]:
        Result = "Result : Man2 Win!"
    elif Man2 == list1[2]:
        Result = "Result : Man1 Win!"
elif Man1 == list1[1]:
    if Man2 == list1[0]:
        Result = "Result : Man1 Win!"
    elif Man2 == list1[1]:
        Result = "Result : Draw"
    elif Man2 == list1[2]:
        Result = "Result : Man2 Win!"
elif Man1 == list1[2]:
    if Man2 == list1[0]:
        Result = "Result : Man2 Win!"
    elif M2an2 == list1[1]:
        Result = "Result : Man1 Win!"
    elif Man2 == list1[2]:
        Result = "Result : Draw"
print(Result)