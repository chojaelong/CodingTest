array = []
visited = []
answer = []
def permutations(n, k):
    global array, visited, answer
    
    for i in range(1, n+1):
        if len(array) == n:
            answer.append(array[::])
            return
        elif visited[i] == False:
            array.append(i)
            visited[i] = True
            permutations(n, k)
            if len(answer) == k:
                return
            array.pop()
            visited[i] = False
            
def solution(n, k):
    global array, visited
    visited = [False] * (n + 1)
    permutations(n, k)
    print()

solution(15, 5)