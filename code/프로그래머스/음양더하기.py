def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        value = absolutes[i] if signs[i] else -absolutes[i]
        sum += value

    return sum