def solution(lottos, win_nums):
    answer = []
    delete = lottos.count(0)
    count = 0
    rank = dict()
    rank[6] = 1
    rank[5] = 2
    rank[4] = 3
    rank[3] = 4
    rank[2] = 5
    for i in lottos:
        if i in win_nums:
            count += 1
    
    return [6 if count+delete <= 2 else rank.get(count+delete), 6 if count < 2 else rank.get(count)]

print(solution([44,1,0,0,31,25], [31,10,45,1,6,19]))