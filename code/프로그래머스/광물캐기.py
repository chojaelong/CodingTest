
min_value = 2000
fatigue = dict()
fatigue["diamond"] = [1, 5, 25]
fatigue["iron"] = [1, 1, 5]
fatigue["stone"] = [1, 1, 1]

def pick(picks, minerals, idx, sum_value):
    global min_value
    
    if idx < len(minerals) and any(picks):
        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1
                values = 0
                for mineral in minerals[idx]:
                    values += fatigue[mineral][i]
                pick(picks, minerals, idx + 1, sum_value + values)
                picks[i] += 1
            else:
                continue
    else:
        min_value = min(sum_value, min_value)

def solution(picks, minerals):
    minerals = [minerals[i : i + 5] for i in range(0, len(minerals), 5)]  
    pick(picks, minerals, 0, 0)
    return min_value

solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])