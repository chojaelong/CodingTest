def solution(n, m, section):
    answer = 0
    paints = [False] * (n + 1)
    for s in section:
        paints[s] = True
    
    for s in section:
        if paints[s]:
            answer += 1
            for i in range(s, m + s):
                if i > n:
                    break
                paints[i] = False
    
    return answer

print(solution(8,4,[2, 3, 6]))