def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    weightidx = len(people) - 1
    exit = [False] * len(people)
    
    for idx, person in enumerate(people):
        if idx > weightidx:
            break
        
        if exit[idx]:
            continue
        
        if person + people[weightidx] <= limit:
            weightidx -= 1
            exit[weightidx] = True
        
        exit[idx] = True
        answer += 1
    
    print(exit)
    return answer

solution([80, 50, 20], 100)