# https://www.acmicpc.net/problem/1026
n = int(input())
a = sorted([int(x) for x in input().split(' ')])
b = sorted([int(y) for y in input().split(' ')], reverse=True)
print(sum([x*y for x, y in zip(a, b)]))

'''alternative'''
#int(input()); print(sum([x*y for x, y in zip(sorted([int(_) for _ in input().split(' ')]), sorted([int(_) for _ in input().split(' ')], reverse=True))]))
