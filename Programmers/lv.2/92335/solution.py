def is_prime(n):
    if n < 2:
        return 0
    elif n%2 == 0:
        return int(n == 2)
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n%i == 0:
                return 0
        return 1

def convert(n: int, k: int):
    if k == 10 or n < k:
        return str(n)

    res = []
    while n > 0:
        res.append(str(n%k))
        n //= k

    return (''.join(res[::-1]))

def solution(n, k):
    converted = []
    for x in convert(n, k).split('0'):
        if x != '':
            converted.append(int(x))
            
    cnt = 0
    for x in converted:
        cnt += is_prime(x)

    return cnt
