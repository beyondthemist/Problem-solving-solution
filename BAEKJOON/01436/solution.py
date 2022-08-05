n = int(input())

count = 0
x = 666 - 1
while count != n:
    x += 1
    if '666' in str(x):
        count += 1
print(x)
