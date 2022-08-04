x, y = 0, 1
for _ in range(int(input())):
    x, y = y, x
    y += x
print(y%10007)
