# https://www.acmicpc.net/problem/2908 

print(max([int(''.join(reversed(list(x)))) for x in input().split()]))
