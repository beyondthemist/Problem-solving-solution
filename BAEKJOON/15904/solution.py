import sys 
input = sys.stdin.readline

s = input().rstrip()
a = 'UCPC'
i, j = 0, 0
n = len(s)
while j < n and i <= 3:
    if s[j] == a[i]:
        i += 1
    j += 1

hate_or_love = 'hate' if i <= 3 else 'love' 
print(f'I {hate_or_love} UCPC')
