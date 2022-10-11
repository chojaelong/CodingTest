# https://www.acmicpc.net/problem/1644

import math

n = int(input())
array = [True for _ in range(n + 1)]
primes = []

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2

        while i * j <= n:
            array[i * j] = False
            j += 1
            
for num in range(2, n + 1):
    if array[num]:
        primes.append(num)

start = 0
end = 0
count = 0

while True:
    result = sum(primes[start : end + 1])
    
    if result > n:
        start += 1
    elif result < n:
        end += 1
    elif result == n:
        count += 1
        end += 1
    
    if start > end or end >= len(primes):
        break

print(count)