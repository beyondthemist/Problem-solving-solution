# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
   return [0 for i in range(n)] if x == 0 else list(range(x, x*(n + 1), x))
