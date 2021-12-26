# https//euler.synap.co.kr/problem=20
# https://projecteuler.net/problem=20

x = 1
for n in range(1, 100):
     x *= n
print(sum([int(i) for i in list(str(x))]))
