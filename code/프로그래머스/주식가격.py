# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices) - 1):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] <= prices[j]:
                if j == len(prices) - 1:
                    answer[i] = count
                    break
                continue
            else:
                answer[i] = count
                break

    return answer

print(solution([1, 2, 3, 2, 3]))