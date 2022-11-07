import sys 
input = sys.stdin.readline

n = [int(c) for c in input().rstrip()]

if sum(n)%3 == 0 and 0 in n:
    print(''.join(sorted([str(x) for x in n], reverse=True)))
else:
    print('-1')
