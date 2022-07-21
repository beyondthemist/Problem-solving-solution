# https://www.acmicpc.net/problem/10809

a = ['-1']*26
s = input()
for i in range(len(s)):
    offset = ord(s[i]) - ord('a')
    if a[offset] == '-1':
        a[offset] = str(i)

print(' '.join(a))
