def solution(n):
    answer = 1
    for i in range(1, n):
        temp = 0
        for v in range(i, n):
            temp += v
            if temp > n:
                break
            elif temp == n:
                answer += 1
                
    return answer
        