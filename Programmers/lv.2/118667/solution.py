from collections import deque

def solution(q1,  q2):
    answer = -2
    cnt = 0
    s1, s2 = sum(q1), sum(q2)
    q1, q2 = deque(q1), deque(q2)
    lim = (len(q1)) << 2
    while s1 != s2 and cnt < lim :
        if s1 > s2:
            v = q1.popleft()
            q2.append(v)
            s1 -= v
            s2 += v
            cnt += 1
        else:
            v = q2.popleft()
            q1.append(v)
            s1 += v
            s2 -= v
            cnt += 1

    answer = cnt if cnt < lim else -1
    return answer
