from collections import deque

def dfs(before, words, visited, target, count):
    if before == target:
        return count
    
    word_length = len(before)
    
    for idx, word in enumerate(words):
        word_agree = [False] * word_length
        for i in range(word_length):
            if before[i] == word[i]:
                word_agree[i] = True
        
        if word_agree.count(True) == word_length - 1 and not visited[idx]:
            visited[idx] = True
            return dfs(word, words, visited, target, count + 1)
            visited[idx] = False
            
def bfs(before, words, target):
    queue = deque([(before, 0)])
    word_length = len(before)
    
    while queue:
        value, c = queue.popleft()
        
        for idx, word in enumerate(words):
            word_agree = [False] * word_length
            for i in range(word_length):
                if value[i] == word[i]:
                    word_agree[i] = True
        
            if word_agree.count(True) == word_length - 1:
                if word == target:
                    return c + 1
                queue.append((value, c + 1))
        
    

def solution(begin, target, words):
    visited = [51] * len(words)
    bfs(begin, words, target)
    idx = words.index(target)
    answer = visited[idx]
    
    if answer == 51:
        return 0
    return answer

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))