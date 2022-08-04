x, y = 0, 1
for _ in range(int(input())):
    x, y = y, x
    y = (x + y)%10007
print(y)
