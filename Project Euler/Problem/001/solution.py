# https://euler.synap.co.kr/problem=1
# https://projecteuler.net/problem=1

print(sum([n if (n%3 == 0 or n%5 == 0) else 0 for n in range(1, 1000)]))
