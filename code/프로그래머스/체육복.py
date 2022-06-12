# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    condition = [True] * (n + 2)

    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))

    for i in real_lost:
        condition[i] = False

    for i in real_reserve:
        if condition[i - 1] == False:
            condition[i - 1] = True
            continue
        elif condition[i + 1] == False:
            condition[i + 1] = True
    
    condition[0] = False
    condition[n + 1] = False

    return condition.count(True)

solution(3, [3], [1])