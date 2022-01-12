# https://programmers.co.kr/learn/courses/30/lessons/62048

def gcd(a, b):
    return b if a%b == 0 else gcd(b, a%b)

def solution(w, h):
    g = gcd(w, h)
    return w*h - ((((w//g) + (h//g)) - 1)*g)
