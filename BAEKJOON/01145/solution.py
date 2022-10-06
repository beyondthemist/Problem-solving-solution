from typing import List
from itertools import combinations

def gcd(a, b):
    if a < b:
        a, b = b, a
    return b if a%b == 0 else gcd(b, a%b)

def lcm(a: List[int], n: int=1) -> int:
    if n == 1:
        return (a[0]*a[1])//gcd(a[0], a[1])
    else:
        val = lcm(a, n - 1)
        return (a[n]*val)//gcd(a[n], val)

a = [int(x) for x in input().split()]
m = a[0]*a[1]*a[2]*a[3]*a[4] #sentinel
for c in combinations(a, 3):
    val = lcm(a=list(c), n=2)
    if m > val:
        m = val

print(m)
