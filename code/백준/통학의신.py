# https://www.acmicpc.net/problem/17945
# x2  + 2Ax + B = 0
import math

A, B = map(int, input().split())
array = []
c = (A * 2) ** 2 - (4 * B)
if c > 0:
    array.append(int((-(A * 2) + math.sqrt(c)) / 2))
    array.append(int((-(A * 2) - math.sqrt(c)) / 2))
elif c == 0:
    array.append(int(-(A * 2) / 2))

array.sort()
print(' '.join(map(str, array)))