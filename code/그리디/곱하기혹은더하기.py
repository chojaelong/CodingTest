import sys

array = list(map(int, input()))
print(array)
blacklist = {0, 1}
sum = 0

for num in array:
    if sum in {0, 1} or num in blacklist:
        sum += num
    else:
        sum *= num

print(sum)