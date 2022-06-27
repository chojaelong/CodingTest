# https://www.acmicpc.net/problem/2609

from math import gcd

a, b = map(int, input().split())
n = gcd(a, b)
print(n, a * b // n, sep=' ')