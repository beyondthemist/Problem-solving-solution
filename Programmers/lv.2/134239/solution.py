from typing import List

def get_hailstone_seq(k: int) -> List[int]:
    n: int = k
    seq: List[int] = [k]

    while n != 1:
        n = n//2 if n%2 == 0 else 3*n + 1
        seq.append(n)

    return seq

def solution(k, ranges):
    seq = get_hailstone_seq(k)
    integrals = [0]
    end = len(seq)
    for i in range(1, end):
        integrals.append((seq[i - 1] + seq[i])/2)
        
    answer = []
    for r in ranges:
        a = r[0]
        b = end - 1 + r[1]
        answer.append(-1 if a > b else sum(integrals[a + 1 : b + 1]))

    return answer
