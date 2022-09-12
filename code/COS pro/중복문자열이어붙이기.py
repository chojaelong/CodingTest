def solution(s1, s2):
	answer = 101
	s1_len = len(s1)
	s2_len = len(s2)
	
	# 뒤 비교
	for i in range(1, min(s1_len, s2_len)):
		temp_s1 = s1[:i]
		temp_s2 = s2[s2_len - i - 1:]
		if temp_s1 == temp_s2:
			answer = s1_len + s2_len - i
			break
			
	# 앞 비교
	for i in range(1, min(s1_len, s2_len)):
		temp_s1 = s1[s1_len - i - 1:]
		temp_s2 = s2[:i]
		if temp_s1 == temp_s2:
			answer = min(answer, s1_len + s2_len - i)
			break
			
	return answer

s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")