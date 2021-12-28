# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total = money - price*(count*(count + 1) // 2)
    return 0 if total >= 0 else -total
