from collections import deque

def time_to_minute(time):
    hour, minute = map(int, time.split(':'))
    return (hour * 60) + minute

def solution(plans):
    plans.sort(key=lambda a: a[1])
    print(plans)
    
    now = time_to_minute(plans[0][1])
    q = deque(plans)
    wait = []
    answer = []
    
    while q or wait:
        if q and time_to_minute(q[0][1]) == now:
            name, start, playtime = q.popleft()
            wait.append([name, int(playtime)])
        
        if wait:
            wait[-1][1] -= 1
            if wait[-1][1] == 0:
                name = wait.pop()[0]
                answer.append(name)
        
        now += 1
    
    return answer
        