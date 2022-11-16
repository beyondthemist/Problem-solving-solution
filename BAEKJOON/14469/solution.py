import sys 
input = sys.stdin.readline

n = int(input())
times = sorted([[int(x) for x in input().split()] for _ in range(n)])

curr = 0
for time in times:
    if curr < time[0]:
        curr = time[0]

    curr += time[1]

print(curr)
