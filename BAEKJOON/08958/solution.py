import sys
input = sys.__stdin__.readline

t = int(input())
for _ in range(t):
    result = input()
    count = 0
    score = 0
    for c in result:
        if c == 'O':
            count += 1
            score += count
        elif c == 'X':
            count = 0
    print(score)
