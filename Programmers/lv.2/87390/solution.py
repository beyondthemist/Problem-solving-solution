def solution(n, left, right):
    answer = []
    for i in range(left//n, (right)//n + 1):
        answer += [i + 1 if j < i else j + 1 for j in range(n)]

    return answer[(left%n):(right - (left//n)*n + 1)]
