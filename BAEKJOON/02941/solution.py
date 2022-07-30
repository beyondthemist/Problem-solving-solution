# https://www.acmicpc.net/problem/2941

s = input()
croatians = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in croatians:
    if c in s:
        s = s.replace(c, 'x')
print(len(s))
