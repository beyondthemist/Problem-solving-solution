# https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    A.sort(); B.sort()

    a = 0
    for i in range(len(A)):
        a += A[i] * B[-1-i]

    return min(a, b)
