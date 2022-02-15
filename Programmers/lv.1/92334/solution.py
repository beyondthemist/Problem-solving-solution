# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    times = {} # id 별 피신고 회수
    ids = {} # 자신이 신고한 id 목록
    answer = [0 for i in range(len(id_list))]
    
    for i in id_list:
        times[i] = 0
        ids[i] = []

    report = list(set(report)) # unique()
    
    for r in report:
        temp = r.split(' ')
        ids[temp[0]].append(temp[1])
        times[temp[1]] += 1
    
    for i in id_list:
        if times[i] >= k:
            for x in ids.keys():
                if i in ids[x]:
                    answer[id_list.index(x)] += 1
    
    return answer
