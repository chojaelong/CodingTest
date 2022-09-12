def number(s):
	first = ord(s[0]) - 65
	second = int(s[1]) - 1
	return first, second

def solution(bishops):
	answer = 0
	array = [[1 for _ in range(8)] for _ in range(8)]
	
	for value in bishops:
		i, j = number(value)
		array[i][j] = 0
		
		while True:
			i += 1
			j += 1
			if i > 7 or j > 7:
				break
			array[i][j] = 0
		
		i, j = number(value)
		while True:
			i += 1
			j -= 1
			if i > 7 or j < 0:
				break
			array[i][j] = 0
			
		i, j = number(value)
		while True:
			i -= 1
			j += 1
			if i < 0 or j > 7:
				break
			array[i][j] = 0
			
		i, j = number(value)
		while True:
			i -= 1
			j -= 1
			if i < 0 or j < 0:
				break
			array[i][j] = 0
	
	for arr in array:
		for value in arr:
			if value == 1:
				answer += 1
	
	return answer

bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")