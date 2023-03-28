from collections import deque

from collections import deque

def solution(n, stations, w):
    answer = 0
    cover = w * 2 + 1
    
    c = 0
    q = deque(stations)

    # 앞부분 조사
    station = q.popleft()
    s = station - w
    if s > 1:
        s_need_cover = s - 1 - c
        answer += s_need_cover // cover
        if s_need_cover % cover > 0:
            answer += 1
    c = station + w

    # 사이 조사
    while q:
        station = q.popleft()
        s = station - w
        m_need_cover = s - c - 1
        answer += m_need_cover // cover
        if m_need_cover % cover > 0:
            answer += 1
        c = station + w

    # 끝 부분 조사
    if c < n:
        e = c
        e_need_cover = n - e
        answer += e_need_cover // cover
        if e_need_cover % cover > 0:
            answer += 1
        c = e
                
    return answer

solution(11, [4, 11], 1)