# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    d = {1: [1, 2, 3, 4, 5],
         2: [2, 1, 2, 3, 2, 4, 2, 5],
         3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    corrects = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(answers)):
        for key in d.keys():
            if answers[i] == d[key][i%len(d[key])]:
                corrects[key] += 1
    
    m = max(corrects.items(), key=lambda x: x[1])[1]
    answer = []
    for i in corrects.keys():
        if m == corrects[i]:
            answer.append(i)
        
    return sorted(answer)
