def solution(name, yearning, photo):
    result = []
    dic = {}
    for i, n in enumerate(name):
        dic[n] = yearning[i]
        
    for p in photo:
        score = 0
        for name in p:
            score += dic.get(name, 0)
        result.append(score)
    
    return result