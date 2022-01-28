# https://programmers.co.kr/learn/courses/30/lessons/81302

from itertools import combinations

def md(c1, c2):
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])

def solution(places):
    answer = []
    for place in places:
        placed = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    placed.append((i, j))

        if placed == []:
            answer.append(1)
            continue
    
        legal = True
        for c in combinations(placed, 2):
            c1 = c[0]
            c2 = c[1]
            
            d = md(c1, c2)
            if d < 2:
                legal = False
            elif d == 2:
                if c1[0] == c2[0]:
                    legal = place[c1[0]][(c1[1] + c2[1]) // 2] == 'X'
                elif c1[1] == c2[1]:
                    legal = place[(c1[0] + c2[0]) // 2][c1[1]] == 'X'
                else:
                    legal = place[c1[0]][c2[1]] == 'X' and place[c2[0]][c1[1]] == 'X'
                    
            if not legal:
                break
                        
        answer.append(1 if legal else 0)
            
    return answer
