import copy
from queue import PriorityQueue

def solution(n, k, enemy):
    temp = copy.deepcopy(enemy)
    length = len(enemy)
    answer = 0
    q = PriorityQueue()
    i = 0
    
    # idx가 라운드를 넘어가지 않으면서 남은 병사가 없거나 무적권이 없을때 까지 반복
    while (n > 0 and i < length) or (k > 0 and i < length):
        n -= enemy[i]
        q.put(-enemy[i])
        
        # 남은 병사가 없을 시 지금까지 방어한 라운드 중 가장 효율적으로 무적권 사용
        if n < 0 and k > 0:
            k -= 1
            value = q.get()
            n -= value
        elif n < 0 and k <= 0:
            break
        
        answer += 1
        i += 1
    
    return answer