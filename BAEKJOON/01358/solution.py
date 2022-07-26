# https://www.acmicpc.net/problem/1358

w, h, base_x, base_y, p = [int(i) for i in input().split()]
count = 0
r = h/2
for _ in range(p):
    x, y = [int(i) for i in input().split()]
    
    #sqaure in center
    if ((x - base_x)**2 + (y - (base_y + r))**2 <= r**2
        or (x - (base_x + w))**2 + (y - (base_y + r))**2 <= r**2
        or (base_x <= x and x <= base_x + w) and (base_y <= y and y <= base_y + h)):
        
        count += 1

print(count)
