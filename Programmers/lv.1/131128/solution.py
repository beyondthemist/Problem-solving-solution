def solution(X, Y):
    count_x = [0]*10
    count_y = [0]*10
    answer = []

    base = ord('0')
    for x in X:
        count_x[ord(x) - base] += 1
    for y in Y:
        count_y[ord(y) - base] += 1

    for i in range(10):
        for _ in range(min(count_x[i], count_y[i])):
            answer.append(str(i))

    if answer:
        answer = ''.join(sorted(answer, reverse=True))
        if len(answer) == answer.count('0'):
            return '0'
    else:
        answer = '-1'
    
    return answer
