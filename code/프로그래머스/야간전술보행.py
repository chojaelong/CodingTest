def solution(distance, scope, times):
    answer = 0
    
    look = [False] * (distance + 1)
    time = [0] * (distance + 1)
    for idx, values in enumerate(scope):
        scope[idx].sort()
        s, e = scope[idx]
        for i in range(s, e + 1):
            look[i] = True
            time[i] = times[idx]
    
    while True:
        answer = answer + 1
        
        if answer > distance:
            return distance
        
        if look[answer]:
            s, e = time[answer]
            find = False
            
            t = answer
            if t > (s + e):
                t = t % (s + e)
            
            if t > 0 and t <= s:
                find = True
                break
            else:
                find = False
                
    return answer

        

solution(12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]])