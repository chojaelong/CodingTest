# https://www.acmicpc.net/problem/1978

import math

def is_prime_number(x):
	# 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            # x가 해당 수로 나누어 떨어진다면
            if x % i == 0:
                return False # 소수가 아님
        return True # 소수임

n = int(input())
array = list(map(int, input().split()))
cnt = 0

for value in array:
    if is_prime_number(value):
        cnt += 1

print(cnt)