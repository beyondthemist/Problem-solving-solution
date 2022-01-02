# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    while len(progresses) >= 1:
        #각 작업의 작업속도 별로 작업 진행
        for i in range(len(progresses)): 
            progresses[i] += speeds[i]
            
        #앞의 작업이 완료되면
        if progresses[0] >= 100: 
            count = 0
            
            #뒤의 모든 작업과 그의 작업속도를 작업 큐에서 제거함
            while len(progresses) >= 1 and progresses[0] >= 100: 
                count += 1
                progresses.pop(0)
                speeds.pop(0)
            answer.append(count)
        
    return answer
