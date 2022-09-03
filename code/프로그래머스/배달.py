# https://school.programmers.co.kr/learn/courses/30/lessons/12978?language=python3
import heapq

INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = 0, 0
# 시작 노드 번호를 입력받기
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = list()
# 최단 거리 테이블을 모두 무한으로 초기화
distance = list()
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = list()


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    global distance, INF
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    global distance, visited
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def solution(N, road, K):
    global graph, distance, visited, n, m
    # 노드의 개수, 간선의 개수를 입력받기
    n, m = N, len(road)
    # 시작 노드 번호를 입력받기
    start = 1
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n + 1)]
    for array in road:
        graph[array[0]].append((array[1], array[2]))
        graph[array[1]].append((array[0], array[2]))
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
    visited = [False] * (n + 1)
    dijkstra(start)

    answer = 1
    for dis in distance:
        if dis <= K and dis != 0:
            answer += 1
    print(distance)
    print(answer)
    return answer

solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)