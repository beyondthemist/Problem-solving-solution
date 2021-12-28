# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = [arr[0], ]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer
