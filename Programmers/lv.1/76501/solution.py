# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] = -absolutes[i]
    
    answer = sum(absolutes)
    return answer
    
    #참고할 만 한 풀이: https://programmers.co.kr/learn/courses/30/lessons/76501/solution_groups?language=python3
    # return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
