#https://www.acmicpc.net/problem/2292

def solution(n):
    if n == 1:
        return 1

    count = 2 #first and last
    tmp = n - 2
    i, a = 0, 1
    while not (6*i <= tmp and tmp < 6*(i + a)):
        count += 1
        i += a
        a += 1
    return count

n = int(input())
print(solution(n))
