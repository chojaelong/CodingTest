def solution(numbers):
    size = len(numbers)
    answer = [-1] * size
    stack = []
    
    for i in range(size):
        if not stack or numbers[i] < numbers[i - 1]:
            stack.append(i)
        else:
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))