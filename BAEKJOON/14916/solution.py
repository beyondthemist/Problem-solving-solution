import sys 
input = sys.stdin.readline

n = int(input())

if n%5 == 0:
    val = n//5
else:
    val = 0
    while n%5 != 0 and n >= 0:
        n -= 2
        val += 1

    val = -1 if n < 0 else (val + (n//5))
        
print(val)
