# https://www.acmicpc.net/problem/10872
# n! = n * (n-1)!

array = [1] * 13
for i in range(2, 13):
    array[i] = array[i-1] * i

print(array[int(input())])
