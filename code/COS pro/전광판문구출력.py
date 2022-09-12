# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(phrases, second):
	answer = ''
	s_len = len(phrases)
	cycle = s_len + 14
	
	while second > cycle:
		second -= cycle
		
	if second < 14:
		while len(answer) != 14 - second:
			answer += '_'
		answer += phrases[:second]
		if len(answer) < 14:
			while len(answer) != 14:
				answer += '_'
	elif second == 14:
		answer += phrases[:second]
	elif second > 14:
		answer += phrases[second - 14 :]
		if len(answer) < 14:
			while len(answer) != 14:
				answer += '_'		
		
	return answer

phrases = "happy"
second = 10
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")