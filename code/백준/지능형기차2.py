array = [list(map(int, input().split())) for _ in range(10)]

temp = 0
maximum = -1

for i in array:
    temp -= i[0]
    temp += i[1]
    maximum = max(temp, maximum)

print(maximum)