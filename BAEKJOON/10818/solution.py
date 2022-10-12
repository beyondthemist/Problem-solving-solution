import sys
input = sys.__stdin__.readline

min = 1000000
max = -1000000
n = int(input())
a = [int(x) for x in input().split()]
for x in a:
    if x < min:
        min = x
    
    if x > max:
        max = x

print(min, max)
