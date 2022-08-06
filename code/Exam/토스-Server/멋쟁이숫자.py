from collections import Counter

def solution(s):
    array = list(map(int, s))
    answer = []
    length = len(array)
    for i in range(length - 2):
        counter = Counter(array[i:i+3])
        if max(counter.values()) == 3:
            value = list(counter.keys())[0]
            answer.append(value)
            
    return max(answer) * 111 if len(answer) != 0 else -1

solution('12223')