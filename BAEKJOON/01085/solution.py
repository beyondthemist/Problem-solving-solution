# https://www.acmicpc.net/problem/1085

x, y, w, h = [int(x) for x in input().split()]
print(min(w - x, x, h - y, y))
