# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    length = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    month = 1; day = 1
    while month != a:
        if day > month:
            day -= length[month - 1]
            month += 1
        else:
            day += 7
    
    idx = day - b - 1 if day > b else b - day 
    answer = days[(days.index('FRI') + (idx))%7]
    return answer
