# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from datetime import datetime
from collections import defaultdict
import math

def solution(fees, records):
    car_times = defaultdict(list)
    for record in records:
        time, number, enter = record.split(' ')
        enter = True if enter == 'IN' else False
        car_times[number].append(time)
        
    car_total_times = []
    for number, times in car_times.items():
        # 입차 출차가 맞지 않을 때
        if len(times) % 2 == 1:
            times.append('23:59')
        
        car_total_times.append([number, 0])
        while times:
            out_time = datetime.strptime(times.pop(), '%H:%M')
            in_time = datetime.strptime(times.pop(), '%H:%M')
            elapsed_time = (out_time - in_time).seconds // 60
            car_total_times[-1][1] += elapsed_time
            
    car_total_times.sort(key = lambda x:(x[0]))    
    answer = []
    for number, minute in car_total_times:
        price = fees[1]
        if minute > fees[0]:
            price += math.ceil((minute - fees[0]) / fees[2]) * fees[3]
        answer.append(price)
        
    return answer