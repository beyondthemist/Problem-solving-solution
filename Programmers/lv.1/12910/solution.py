# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    l = sorted([n for n in arr if n%divisor == 0])
    return [-1] if len(l) == 0 else l 
