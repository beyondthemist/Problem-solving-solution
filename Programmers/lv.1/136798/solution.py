from math import sqrt

def get_divisors_num(n):
    cnt = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n%i == 0:
            cnt += 2

    return cnt - int(sqrt(n) - int(sqrt(n)) == 0)

def solution(number, limit, power):
    answer = 0
    for knight in range(1, number + 1):
        n = get_divisors_num(knight)
        answer += n if n <= limit else power
        
    return answer
