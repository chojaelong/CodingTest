import datetime
from collections import defaultdict

def solution(book_time):
    answer = 0
    rooms = defaultdict(list)
    
    for i in range(len(book_time)):
        start_time = datetime.datetime.strptime(book_time[i][0], '%H:%M')
        end_time = datetime.datetime.strptime(book_time[i][1], '%H:%M')
        # 청소시간 연산
        end_time = end_time + datetime.timedelta(minutes=10)
        
        for idx, room in rooms.items():
            for hours in room:
                # 시작 시간과 끝 시간이 비교 대상 시간에 포함될 경우
                if (hours[0] <= start_time < hours[1]) or (hours[0] < end_time <= hours[1]) or not(start_time < hours[0] < end_time):
                    break
            
            # 해당 방의 예약이 겹치지 않은 경우
            else:
                rooms[idx].append((start_time, end_time))
                break
        
        
        # 새로운 방이 필요한 경우
        else:
            rooms[answer].append((start_time, end_time))
            answer += 1
        
    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))