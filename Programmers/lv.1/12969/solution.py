# https://programmers.co.kr/learn/courses/30/lessons/12954

n, m = map(int, input().strip().split(' '))
print(''.join(['*']*n + ['\n'])*m)
