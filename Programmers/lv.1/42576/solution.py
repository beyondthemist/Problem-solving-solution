#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    dic = {participant[0]: 1}
    for i in range(1, len(participant)):
        if participant[i] in dic:
            dic[participant[i]] = dic[participant[i]] + 1
        else:
            dic[participant[i]] = 1
    
    for i in range(0, len(completion)):
        if completion[i] in dic:
            dic[completion[i]] = dic[completion[i]] - 1

    for i in range(0, len(participant)):
        if dic[participant[i]] > 0:
            return participant[i]

    return ''
