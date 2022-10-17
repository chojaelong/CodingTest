def solution(elements):
    length = len(elements)
    array = elements * 2
    values = []
    
    for i in range(1, length + 1):
        for j in range(length):
            values.append(sum(array[j : j + i]))
            
    return len(set(values))