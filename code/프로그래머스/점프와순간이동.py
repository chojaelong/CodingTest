def solution(n):
    answer = 1
    while n != 1:
        if n % 2 == 1:
            n -= 1
            answer += 1
        else:
            n //= 2
    
    return answer

solution(5000)