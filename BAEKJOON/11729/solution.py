# https://www.acmicpc.net/problem/11729

def move(n, src, dst, tmp):
    if n >= 1:
        move(n - 1, src, tmp, dst)
        print(src, dst)
        move(n - 1, tmp, dst, src)
        
n = int(input())
print(2**n - 1)
move(n, 1, 3, 2)
