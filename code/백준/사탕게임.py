import sys
input=sys.stdin.readline

# True : 좌 우 바꾸기
# False : 상 하 바꾸기
def solution(a, b, bool, candy):
    global n

    # Swap
    if bool:
        candy[a][b], candy[a][b + 1] = candy[a][b + 1], candy[a][b]
    elif not bool:
        candy[a][b], candy[a + 1][b] = candy[a + 1][b], candy[a][b]
    
    max_value = 1
    # 양 옆 계산
    temp = 1
    for i in range(n):
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                temp += 1
            else:
                temp = 1
            max_value = max(temp, max_value)
        temp = 1

    # 위 아래 계산
    temp = 1
    for j in range(n):
        for i in range(n-1):
            if candy[i][j] == candy[i+1][j]:
                temp += 1
            else:
                temp = 1
            max_value = max(temp, max_value)
        temp = 1

    
    # 바꿨던 원소 다시 원래대로 돌리기
    if bool:
        candy[a][b], candy[a][b + 1] = candy[a][b + 1], candy[a][b]
    elif not bool:
        candy[a][b], candy[a + 1][b] = candy[a + 1][b], candy[a][b]

    return max_value


n = int(input())
array = [list(input()) for _ in range(n)]
max_value = 0

# 일반적인 경우 : 양옆 swap 후 위아래 swap
# x의 위치가 배열의 마지막일 경우 : 위아래만 swap
# y의 위치가 배열의 마지막일 경우 : 양옆만 swap
# x, y의 위치가 배열의 마지막일 경우 : 순회 중단
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
