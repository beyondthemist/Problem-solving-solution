# https://programmers.co.kr/learn/courses/30/lessons/12940

def gcd(a, b):
    return gcd(b, a%b) if a%b != 0 else b

def solution(n, m):
    g = gcd(max(n, m), min(n, m))
    return [g, n*m//g]
