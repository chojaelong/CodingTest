def solution(ingredient):
    stack = []
    answer = 0
    
    for value in ingredient:
        stack.append(value)
        
        if len(stack) >= 4:
            if stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
                
    return answer