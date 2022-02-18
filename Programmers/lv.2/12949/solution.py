# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = list()
    for i in range(len(arr1)):
        answer.append(list())
        for j in range(len(arr2[0])):
            val = 0
            for k in range(len(arr1[i])):
                val += arr1[i][k] * arr2[k][j]
            answer[i].append(val)
    
    return answer
