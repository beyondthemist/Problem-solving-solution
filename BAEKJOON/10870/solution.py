# https://www.acmicpc.net/problem/10870

def f(n):
    return f(n - 1) + f(n - 2) if n > 1 else n

print(f(int(input())))
