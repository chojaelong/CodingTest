def change(word, skip):
    idx = ord(word) + 1
    if idx == ord('z') + 1:
        idx = ord('a')
    word = chr(idx)
    if word in skip:
        return change(word, skip)
    return word

def solution(s, skip, index):
    array = list(s)
    skips = list(skip)
    answer = ''
    
    for word in array:
        for i in range(index):
            word = change(word, skip)
        answer += word
    
    return answer