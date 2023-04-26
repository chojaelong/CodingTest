def solution(code):
    mode = 0
    array = list(code)
    answer = ''
    
    for idx, word in enumerate(array):
        if word == "1":
            mode = (mode + 1) % 2
        else:
            if idx % 2 == mode:
                answer += word
    
    return "EMPTY" if len(answer) == 0 else answer