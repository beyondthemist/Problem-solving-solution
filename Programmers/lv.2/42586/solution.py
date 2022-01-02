# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    while len(progresses) >= 1:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            count = 0

            while len(progresses) >= 1 and progresses[0] >= 100:
                count += 1
                progresses.pop(0)
                speeds.pop(0)
            answer.append(count)
        
    return answer
