# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count = 0
    while num != 1 and count <= 500:
        num = num//2 if num%2 == 0 else 3*num + 1        
        count += 1
    return count if count <= 500 else -1
