# https://euler.synap.co.kr/problem=31
# https://projecteuler.net/problem=31

pences = [1, 2, 5, 10, 20, 50, 100, 200]
count = 0
pmt = 200
d = [1] + ([0]*(pmt)) #[1]: sentinel

for pence in pences:
     for i in range(pence, pmt + 1):
          d[i] += d[i - pence]
     
print(d[-1])
