# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    s = set()
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            s.add(int(''.join(p)))
    
    sieve = [False if x%2 == 0 else True for x in range(max(s) + 1)]
    sieve[1] = False; sieve[2] = True
    
    answer = 0
    for i in range(3, len(sieve), 2):
        if sieve[i]:
            for j in range(2*i, len(sieve), i):
                sieve[j] = False
                
    for number in s:
        if sieve[number]:
            answer += 1
    
    return answer
