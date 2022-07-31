# https://www.acmicpc.net/problem/1316 

count = 0
for _ in range(int(input())):
    l = [0]*26
    prev = None
    is_grouped = True
    for c in input():
        offset = ord(c) - ord('a')
        if prev != c:
            if l[offset] != 0:
                is_grouped = False
                break
            prev = c
        l[offset] += 1
    if is_grouped:
        count += 1
print(count)
