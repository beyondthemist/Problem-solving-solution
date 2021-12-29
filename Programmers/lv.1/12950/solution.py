# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    return [[e1 + e2 for e1, e2 in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]
