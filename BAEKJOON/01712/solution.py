#https://www.acmicpc.net/problem/1712

fc, vc, p = [int(x) for x in input().split()]
print(-1 if vc >= p else (fc//(p - vc)) + 1)
