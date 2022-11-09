import sys 
input = sys.stdin.readline

n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))

count = 0
for i in range(n - 1, 0, -1):
    if scores[i - 1] >= scores[i]:
        count += (scores[i - 1] - scores[i] + 1)
        scores[i - 1] -= (scores[i - 1] - scores[i] + 1)

print(count)
