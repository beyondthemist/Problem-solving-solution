# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    is_prime = [False]*2 + [True] + [i%2 == 0 for i in range(n - 2)]
    i = 3
    while i*i <= len(is_prime):
        if is_prime[i]:
            for j in range(2*i, len(is_prime), i):
                is_prime[j] = False
        i += 2
    answer = len([i for i in range(len(is_prime)) if is_prime[i]])
    return answer
