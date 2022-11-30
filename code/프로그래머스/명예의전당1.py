def solution(k, score):
    answer = []
    queue = []
    
    for s in score:
        size = len(queue)
        
        if size < k:
            queue.append(s)
            queue.sort(reverse=True)
            answer.append(queue[-1])
            
        elif size == k:
            if queue[-1] < s:
                queue.pop()
                queue.append(s)
                queue.sort(reverse=True)
            
            answer.append(queue[-1])
    
    return answer