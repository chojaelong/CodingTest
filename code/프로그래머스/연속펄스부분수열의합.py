def solution(sequence):
    pers = [1, -1]
    length = len(sequence)
    pers1 = [pers[i % 2] for i in range(length)]
    pers2 = [pers[i % 2] for i in range(1, length + 1)]
    array1 = [sequence[i] * pers1[i] for i in range(length)]
    array2 = [sequence[i] * pers2[i] for i in range(length)]
    
    dp1 = [0] * length
    dp1[0] = array1[0]
    for i in range(1, length):
        dp1[i] = max(array1[i], dp1[i - 1] + array1[i])
        
    dp2 = [0] * length
    dp2[0] = array2[0]
    for i in range(1, length):
        dp2[i] = max(array2[i], dp2[i - 1] + array2[i])
    
    answer = max(max(dp1), max(dp2))
    return answer