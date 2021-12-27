n1, n2 = 1; n3 = 0
count = 2

while len(str(n3)) < 1000:
     count += 1
     n3 = n1 + n2
     n1 = n2
     n2 = n3

print(count)
