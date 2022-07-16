# https://www.acmicpc.net/problem/1463

m = [0, 0, 1, 1]
n = int(input())
for i in range(4, n + 1):
    if i%3 == 0 and i%2 == 0:
        m.append(1 + min(m[i - 1], m[i//3], m[i//2]))
    elif i%3 == 0:
        m.append(1 + min(m[i - 1], m[i//3]))
    elif i%2 == 0:
        m.append(1 + min(m[i - 1], m[i//2]))    
    else:
        m.append(1 + m[i - 1])

print(m[n])
