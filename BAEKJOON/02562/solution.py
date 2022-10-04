x, idx = -1, 0
for i in range(9):
    v = int(input())
    if x < v:
        x = v
        idx = i

print(x, (idx + 1), sep='\n')
