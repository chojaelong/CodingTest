def solution(n):
    question = bin(n)[2:]
    q_array = list(question)
    q_one = q_array.count('1')
    
    for i in range(n + 1, 1000001):
        answer = bin(i)[2:]
        a_array = list(answer)
        a_one = a_array.count('1')
        if q_one == a_one:
            return i
