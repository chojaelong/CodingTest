import math

def is_prime_number(x):
	# 2부터 x의 제곱근까지의 모든 수를 확인하며
	for i in range(2, int(math.sqrt(x)) + 1):
		# x가 해당 수로 나누어 떨어진다면
		if x % i == 0:
			return False # 소수가 아님
	return True # 소수임

def solution(nums):
    iter = len(nums)
    count = 0
    for i in range(iter - 2):
        for j in range(i + 1, iter - 1):
            for k in range(j + 1, iter):
                if is_prime_number(nums[i] + nums[j] + nums[k]):
                    count += 1
    
    return count