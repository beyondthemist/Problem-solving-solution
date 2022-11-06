# https://programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil 

def solution(fees, records):
    default_time, default_fee, time_unit, fee_unit = fees[0], fees[1], fees[2], fees[3]

    parked = {} # car: point of IN/OUT
    total_time = {} # car: cumulative time
    for record in records:
        data = record.split()
        time, car, flag = data[0], data[1], data[2]
        
        if flag == "IN":
            parked[car] = int(time[:2])*60 + int(time[3:])
        else:
            parked_time = int(time[:2])*60 + int(time[3:]) - parked.pop(car)
            total_time[car] = total_time.get(car, 0) + parked_time
            
    for car in parked:
        total_time[car] = total_time.get(car, 0) + ((23*60 + 59) - parked[car])
    
    answer = []
    for car in sorted(total_time):
        answer.append(default_fee + ceil(max(total_time[car]-default_time, 0)/time_unit)*fee_unit)
        
    return answer
