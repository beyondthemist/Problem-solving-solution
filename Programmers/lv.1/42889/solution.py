# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    fail_rate = {}
    for i in range(1, N + 1):
        not_cleared = reached = 0
        for j in range(len(stages)):
            if stages[j] > i:
                reached = reached + 1
            elif stages[j] == i:
                not_cleared = not_cleared + 1
                reached = reached + 1
        
        if reached != 0:
            fail_rate[i] = not_cleared/reached
        else:
            fail_rate[i] = 0

    fail_rate = sorted(fail_rate.items(), reverse=True, key=lambda x: x[1])
    
    answer = []
    for i in range(len(fail_rate)):
        answer.append(fail_rate[i][0])
    
    return answer
