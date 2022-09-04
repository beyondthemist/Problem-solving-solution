n, m = [int(x) for x in input().split()]
a = set([int(y) for y in input().split()])
b = set([int(z) for z in input().split()])
print(len((a - b).union(b - a)))
