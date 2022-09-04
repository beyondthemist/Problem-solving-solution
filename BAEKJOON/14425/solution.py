# https://www.acmicpc.net/problem/14425

n, m = [int(x) for x in input().split()]
str_set = set([input() for _ in range(n)])
strs_to_test = [input() for _ in range(m)]

count = 0
for s in strs_to_test:
    if s in str_set:
        count += 1
print(count)
