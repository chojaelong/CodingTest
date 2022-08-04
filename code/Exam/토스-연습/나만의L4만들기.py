from collections import deque

def next_server(servers):
    servers_len = [len(servers[i]) for i in range(len(servers))]
    min_index = servers_len.index(min(servers_len))
    return min_index

# server : 총 서버 갯수
# sticky : 라운드 로빈 여부
# requests : 요청한 클라이언트 번호
def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    
    # 라운드 로빈으로 동작할 경우
    if not sticky:
        queue = deque(requests)
        now_server = 0
        
        while queue:
            request = queue.popleft()
            answer[now_server].append(request)
            now_server = next_server(answer)
        
        return answer
    
    # 라운드 로빈 방식이 아닌 경우
    elif sticky:
        queue = deque(requests)
        now_server = 0
        
        while queue:
            request = queue.popleft()
            condition = False
            
            for i in range(len(answer)):
                if answer[i].count(request) != 0:
                    condition = True
                    now_server = i
            
            answer[now_server].append(request)
            now_server = next_server(answer)
        
        return answer
    
print(solution(2, True, [1, 2, 2, 3, 4, 1]))