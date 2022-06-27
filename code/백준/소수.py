import math

m = int(input())
n = int(input())
# 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(10001)]
array[0] = False
array[1] = False

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지 모든 수를 확인하며
for i in range(2, int(math.sqrt(10000)) + 1):
	if array[i] == True: # i가 소수인 경우(남은 수인 경우)
		# i를 제외한 i의 모든 배수를 지우기
		j = 2
		while i * j <= 10000:
			array[i * j] = False
			j += 1

answer = array[m : n + 1]
value = 0

if len(answer) == answer.count(False):
    print(-1)
else:
    sum = 0
    for i in range(m, n + 1):
        if array[i] == True:
            sum += i

    for i in range(m, n + 1):
        if array[i] == True:
            value = i
            break
    print(sum)
    print(value)