# 2 x 1 = 2
# . . . . .
# ************
# 3 x 1 = 3
# . . . . .
# ************
# . . . . .

for i in range(2, 10):
    print("*****************")
    for j in range(1, 10):
        print(i, "x", j ,"=", i*j)