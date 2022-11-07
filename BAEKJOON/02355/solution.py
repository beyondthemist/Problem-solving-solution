import sys
input = sys.__stdin__.readline
a, b = [int(x) for x in input().split()]
if a > b:
    a, b = b, a
print( ((b*(b + 1))//2) - (((a*(a - 1))//2)) )
