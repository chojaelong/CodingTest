# https://school.programmers.co.kr/learn/courses/30/lessons/84512

import sys

word = []
words = []
array = ['A', 'E', 'I', 'O', 'U']

def back_tracking():
    global word, words, array
    length = len(word)
    if length >= 5:
        return
    for w in array:
        word.append(w)
        words.append(''.join(word))
        back_tracking()
        word.pop()
        

def solution(word):
    sys.setrecursionlimit(10000000)
    back_tracking()
    
    answer = words.index(word)
    return answer + 1

solution('AAAAE')