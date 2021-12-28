# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    #hor = [max(size) for size in sizes]
    #ver = [min(size) for size in sizes]
    
    return max([max(size) for size in sizes])*max([min(size) for size in sizes])
