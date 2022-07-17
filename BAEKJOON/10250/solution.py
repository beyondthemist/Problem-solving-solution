# https://www.acmicpc.net/problem/10250

for i in range(int(input())):
    h, w, n = [int(x) for x in input().split()]
    print('{}{:0>2}'.format(((n - 1)%h) + 1,  ((n - 1)//h) + 1))
