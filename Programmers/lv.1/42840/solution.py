# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    d = {1: [1, 2, 3, 4, 5],
         2: [2, 1, 2, 3, 2, 4, 2, 5],
         3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    corrects = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(answers)):
        if answers[i] == d[1][i%len(d[1])]:
            corrects[1] += 1
        if answers[i] == d[2][i%(len(d[2]))]:
            corrects[2] += 1
        if answers[i] == d[3][i%(len(d[3]))]:
            corrects[3] += 1
    
    m = max(corrects.items(), key=lambda x: x[1])[1]
    answer = []
    for i in list(corrects.keys()):
        if m == corrects[i]:
            answer.append(i)
        
    return sorted(answer)
