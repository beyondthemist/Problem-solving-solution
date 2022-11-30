def solution(k, scores):
    hof = []
    answer = []

    for score in scores:
        hof.append(score)
        hof.sort()
        if len(hof) > k:
            hof.pop(0)
        answer.append(hof[0])

    return answer
