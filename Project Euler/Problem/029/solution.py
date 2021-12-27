#https://euler.synap.co.kr/problem=29
#https://projecteuler.net/problem=29

l = []
for a in range(2, 101):
     for b in range(2, 101):
          if a**b not in l:
               l.append(a**b)
print(len(l))
