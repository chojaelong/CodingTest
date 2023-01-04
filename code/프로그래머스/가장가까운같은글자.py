def solution(s):
    array = list(set(s))
    d = dict()
    answer = []
    
    for word in array:
        d[word] = -1
    
    for idx, word in enumerate(s):
        if d[word] == -1:
            answer.append(-1)
        else:
            answer.append(idx - d[word])
        d[word] = idx
        
    return answer