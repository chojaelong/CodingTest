from collections import deque

def bfs(n, info):
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    n_gap = 0
    res = []
    
    while q:
        focus, arrow = q.popleft()
        
        # 화살 다 쏜 경우
        if sum(arrow) == n:
            lion, apeach = 0, 0
            for i in range(11):
                if info[i] != 0 or arrow[i] != 0:
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            
            if lion > apeach:
                gap = lion - apeach
                if n_gap <= gap:
                    n_gap = gap
                    res.append(arrow)
            
        
        # 화살 더 쏜 경우
        elif sum(arrow) > n:
            continue
            
        # 화살 덜 쏜 경우
        elif focus == 10:
            extra = n - sum(arrow)
            arrow[focus] = extra
            q.append((-1, arrow))
        
        # 화살 쏘기
        else:
            # 어피치보다 한발 많이 쏘기
            temp1 = arrow.copy()
            temp1[focus] = info[focus] + 1
            q.append((focus + 1, temp1))
            
            # 0발 쏘기
            temp2 = arrow.copy()
            q.append((focus + 1, temp2))
            
    return res
            

def solution(n, info):
    array = bfs(n, info)
    if len(array) == 0:
        return [-1]
    else:
        return array[-1]