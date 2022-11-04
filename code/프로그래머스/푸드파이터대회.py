def solution(food):
    answer = ''
    for i in range(1, len(food)):
        value = food[i]
        if value % 2 == 1:
            value -= 1
        answer += str(i) * (value // 2)
    
    return (answer + '0' + answer[::-1])
        