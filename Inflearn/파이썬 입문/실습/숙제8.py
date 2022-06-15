result = ''
one = 0
two = 0
three = 0

for i in range(100, 301):
    one = i // 100
    two = (i // 10) % 10
    three = i % 10
    if one % 2 == 0 and two % 2 == 0 and three % 2 == 0:
        result += str(i) + ","
print(result[:-1])