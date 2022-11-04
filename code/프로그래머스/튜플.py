from collections import Counter

def solution(s):
    str1 = s.replace('{', '[')
    str1 = str1.replace('}', ']')
    array = eval(str1)
    array.sort(key=lambda x: len(x))
    answer = []
    
    temp = []
    for arr in array:
        c1 = Counter(arr)
        c2 = Counter(temp)
        
        c3 = c1 - c2
        answer.append(c3.most_common()[0][0])
        temp = arr
        
    return answer
    