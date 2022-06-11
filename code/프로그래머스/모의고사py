def solution(answers):
    student1 = [1, 2, 3, 4, 5] * 2000
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    answer1 = check(answers, student1)
    answer2 = check(answers, student2)
    answer3 = check(answers, student3)

    max_value = max(answer1, answer2, answer3)

    array = []

    if answer1 == max_value: array.append(1)
    if answer2 == max_value: array.append(2)
    if answer3 == max_value: array.append(3)

    return array

def check(answer, array):
    count = 0
    for i in range(len(answer)):
        if answer[i] == array[i]:
            count += 1
    
    return count

solution(	[1, 3, 2, 4, 2])