from collections import Counter

def solution(topping):
    length = len(topping)
    answer = 0
    s = set([])
    dic = Counter(topping)
    
    
    for i in range(length):
        s.add(topping[i])
        dic[topping[i]] -= 1
        if dic[topping[i]] == 0:
            dic.pop(topping[i])
        if len(s) == len(dic):
            answer += 1
    
    return answer