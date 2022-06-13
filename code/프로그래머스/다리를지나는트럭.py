from collections import deque
def solution(bridge_length, weight, truck_weights):
    ing = deque([0] * bridge_length)
    wait = deque(truck_weights)
    end = []
    now_weight = 0
    now_bridge = 0
    sec = 0

    value = wait.popleft()
    ing.pop()
    ing.append(value)
    now_weight += value
    now_bridge += 1

    sec += 1

    while wait:
        if len(ing) > 0:
            value = ing.popleft()
            ing.append(0)
            if value != 0:
                end.append(value)
                now_bridge -= 1
                now_weight -= value

        if now_bridge + 1 <= bridge_length and now_weight + wait[0] <= weight:
            value = wait.popleft()
            ing.pop()
            ing.append(value)
            now_weight += value
            now_bridge += 1

        sec += 1
    
    while ing.count(0) != bridge_length:
        value = ing.popleft()
        ing.append(0)
        if value != 0:
            end.append(value)
            now_bridge -= 1
            now_weight -= value
        sec += 1

    return sec
        
        



print(solution(2, 10, [7, 4, 5, 6]))