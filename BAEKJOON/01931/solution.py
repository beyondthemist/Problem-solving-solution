import sys
imput = sys.__stdin__.readline

n = int(input().rstrip())

schedules = sorted(
    [tuple([int(x) for x in input().split()]) for _ in range(n)],
    key=lambda item: item[0])
schedules = sorted(schedules, key=lambda item: item[1])

answer = [schedules[0]]
for i in range(1, n):
    if answer[-1][1] <= schedules[i][0]:
        answer.append(schedules[i])

print(len(answer))
