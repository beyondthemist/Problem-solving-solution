# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(bridge_length, weight, truck_weights):
    seconds = 0
    bridge = [] # [truck, passed_seconds]
    while len(bridge) != 0 or len(truck_weights) != 0:
        seconds += 1
        for i in range(len(bridge)):
            bridge[i][1] += 1
            if bridge[i][1] == bridge_length:
                del bridge[i]
            
        if (len(truck_weights) > 0 and
            bridge_length - len(bridge) > 0 and 
            truck_weights[0] <= weight - sum([bridge[i][0] for i in range(len(bridge))])):
            bridge.insert(0, [truck_weights.pop(0), 0])
        
    return seconds
