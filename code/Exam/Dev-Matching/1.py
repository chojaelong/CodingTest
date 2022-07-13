# 

def solution(grade):
    answer = 0
    min_value = min(grade)

    if grade[0] > min_value:
        answer += grade[0] - min_value
        grade[0] = min_value

    for i in range(1, len(grade)):
        min_value = min(grade[i:])
        if grade[i] > min_value:
            answer += grade[i] - min_value
            grade[i] = min_value

        if grade[i-1] > grade[i]:
            answer += grade[i-1] - grade[i]
            grade[i-1] = grade[i]

    return answer

solution([3, 2, 3, 6, 4, 3, 7])
