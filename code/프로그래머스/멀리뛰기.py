# 1 2 3 5 8 13 21 
# f(x) = f(x-2) + f(x-1)

n = int(input())

array = [0] * 2001
array[1] = 1
array[2] = 2

for i in range(3, len(array) - 1):
    array[i] = array[i-2] + array[i-1]

print(array[n] % 1234567)

