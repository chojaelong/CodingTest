from collections import Counter

# True : 좌 우 바꾸기
# False : 상 하 바꾸기
def solution(a, b, bool, array):
    global n
    if bool:
        array[a][b], array[a][b + 1] = array[a][b + 1], array[a][b]
    elif not bool:
        array[a][b], array[a + 1][b] = array[a + 1][b], array[a][b]
    counter = list(Counter(array[i]) for i in range(n))
    return 1


n = int(input())
array = [list(input()) for _ in range(n)]
max_value = 0
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        elif i == n-1:
            max_value = max(max_value, solution(i, j, True, array))
        elif j == n-1:
            max_value = max(max_value, solution(i, j, False, array))
        else:
            max_value = max(max_value, solution(i, j, True, array))
            max_value = max(max_value, solution(i, j, False, array))

print(max_value)
