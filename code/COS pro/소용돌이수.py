def solution(n):
	array = [[0 for _ in range(n)] for _ in range(n)]
	# 0: 오, 1: 밑, 2: 왼, 3: 위
	dir = 0
	
	num = 1
	i, j = 0, 0
	while num != n**2:
		array[i][j] = num
		num += 1
		
		if dir == 0:
			if j + 1 == n or array[i][j + 1] != 0:
				dir += 1
				i += 1
			else:
				j += 1
		elif dir == 1:
			if i + 1 == n or array[i + 1][j] != 0:
				dir += 1
				j -= 1
			else:
				i += 1
		elif dir == 2:
			if i - 1 == -1 or array[i - 1][j] != 0:
				dir += 1
				i -= 1
			else:
				j -= 1
		elif dir == 3:
			if j - 1 == -1 or array[i][j - 1] != 0:
				dir = 0
				j += 1
			else:
				i -= 1
	
	print(array)
	
	answer = 0
	for i in range(n):
		answer += array[i][i]
	return answer

n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")