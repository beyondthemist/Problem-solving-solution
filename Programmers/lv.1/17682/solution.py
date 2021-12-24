#https://programmers.co.kr/learn/courses/30/lessons/17682

import re

def solution(dartResult):
    bonus_table = {'S': 1, 'D': 2, 'T': 3}
    option_table = {'*': 2, '#': -1}
    
    digits = re.compile('[\d]+').findall(dartResult)
    bonuses = re.compile('[SDT](?:[*#])?').findall(dartResult)
    
    scores = [0, ]
    for i in range(len(digits)):
        score = int(digits[i])
        bonus = bonuses[i]
        
        score = score**(bonus_table.get(bonus[0]))
        if len(bonus) >= 2:
            option_key = bonus[-1]
            score = score * option_table.get(option_key)
            
            if option_key == '*':
                scores[-1] = scores[-1] * option_table.get(bonus[-1])
        
        scores.append(score)
        
    answer = sum(scores)
    return answer
