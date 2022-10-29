def solution(n):
    total = sum([i for i in range(n + 1)])
    start_arr = [[] for _ in range(n)]
    end_arr = [[] for _ in range(n)]
    
    repeat = n
    idx = 0
    now = 1
    
    while repeat > 0:
        for _ in range(repeat):
            start_arr[idx].append(now)
            now += 1
            idx += 1
        
        idx -= 1
        repeat -= 1
        if repeat == 0:
            break
        
        for _ in range(repeat):
            start_arr[idx].append(now)
            now += 1
        
        idx -= 1
        repeat -= 1
        
        for _ in range(repeat):
            end_arr[idx].append(now)
            now += 1
            idx -= 1
        
        idx += 2
        repeat -= 1
        
    total_arr = []
    for idx in range(n):
        total_arr.extend(start_arr[idx])
        end_arr[idx].reverse()
        total_arr.extend(end_arr[idx])
    
    return total_arr
            
            