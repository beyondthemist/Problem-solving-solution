#https://www.acmicpc.net/problem/2869

from math import ceil
a, b, v = [int(x) for x in input().split()]
print(1 + ceil((v - a)/(a - b)))
