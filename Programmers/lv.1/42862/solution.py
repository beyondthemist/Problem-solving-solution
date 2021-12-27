# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserves = sorted(list(set(reserve) - set(lost)))
    losts = sorted(list(set(lost) - set(reserve)))
    
    i = 0
    while i in range(len(losts)):
        lost_student = losts[i]
        if lost_student - 1 in reserves:
            losts.remove(lost_student)
            reserves.remove(lost_student - 1)
        elif lost_student + 1 in reserves:
            losts.remove(lost_student)
            reserves.remove(lost_student + 1)
        else:
            i += 1

    answer = n - len(losts)
    
    return answer
