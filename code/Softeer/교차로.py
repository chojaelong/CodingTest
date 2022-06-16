import sys
from collections import deque

queues = dict()
queues["A"] = deque()
queues["B"] = deque()
queues["C"] = deque()
queues["D"] = deque()
array = deque()

n = int(input())
for i in range(n):
    array.append(list(map(str, input().split())))

result = [-1] * len(array)
count = 0
for i in range(50000):
    drive = [False] * 4
    # 더 이상 진입할 차와 빠져나갈 차가 없을 때
    if not array and not queues["A"] and not queues["B"] and not queues["C"] and not queues["D"]:
        break

    # 교착상태 일 때
    if queues["A"] and queues["B"] and queues["C"] and queues["D"]:
        break

    # 해당 시간에 진입 한 차량들에 대한 대기 큐 삽입
    while array:
        if array[0][0] == str(i):
            queues[array[0][1]].append(count)
            array.popleft()
            count += 1
        else:
            break

    # 차량 진행
    # A 진행
    if queues["A"] and not queues["D"]:
        drive[0] = True       
    # B 진행
    if queues["B"] and not queues["A"]:
        drive[1] = True
    # C 진행
    if queues["C"] and not queues["B"]:
        drive[2] = True
    # D 진행
    if queues["D"] and not queues["C"]:
        drive[3] = True

    if drive[0] == True:
        key = queues["A"].popleft()
        result[key] = i
    if drive[1] == True:
        key = queues["B"].popleft()
        result[key] = i
    if drive[2] == True:
        key = queues["C"].popleft()
        result[key] = i
    if drive[3] == True:
        key = queues["D"].popleft()
        result[key] = i

for i in result:
    print(i)

            