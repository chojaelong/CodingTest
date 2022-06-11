from collections import deque

def solution(progresses, speeds):
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)
    answer = []
    while progresses_queue:
        count = 0
        for i in range(len(progresses_queue)):
            progresses_queue[i] += speeds_queue[i]
        
        while progresses_queue:
            if progresses_queue[0] >= 100:
                progresses_queue.popleft()
                speeds_queue.popleft()
                count += 1
            else:
                break
        if count > 0:
            answer.append(count)

    return answer
