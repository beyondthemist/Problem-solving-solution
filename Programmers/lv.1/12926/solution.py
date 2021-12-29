# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    A_Z = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
    a_z = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    s = list(s)

    for i in range(len(s)):
        if s[i] in A_Z:
            s[i] = A_Z[(A_Z.index(s[i]) + n)%len(A_Z)]
        elif s[i] in a_z:
            s[i] = a_z[(a_z.index(s[i]) + n)%len(a_z)]

    answer = ''.join(s)
    return answer
