import heapq

def solution(scoville, K):
    count = 0
    scoville_condition = [False] * len(scoville)

    for i in range(len(scoville)):
        if scoville[i] >= K:
            scoville_condition[i] = True
    
    dismatch = scoville_condition.count(False)

    heapq.heapify(scoville)

    while dismatch > 0:
        if len(scoville) == 0 or len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        dismatch -= 2
        new_scoville = a + (b * 2)
        heapq.heappush(scoville, new_scoville)
        if new_scoville < K:
            dismatch += 1

        count += 1

    return count

scoville = [1, 2, 3, 9, 10, 12]
K = 7
solution(scoville, K)