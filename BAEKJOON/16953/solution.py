import sys

input = sys.__stdin__.readline
sys.setrecursionlimit(10**5)

def dfs(a: int, b: int, count=1) -> int:
    if a > b:
        return -1
    elif a == b:
        return count
    else:
        res1 = dfs(2*a, b, count + 1)
        res2 = dfs(10*a + 1, b, count + 1)

        if res1 == -1 and res2 == -1:
            return -1
        elif res1 != -1 and res2 != -1:
            return min(res1, res2)
        else:
            return res1 if res1 != -1 else res2

a, b = [int(x) for x in input().split()]
print(dfs(a, b))
