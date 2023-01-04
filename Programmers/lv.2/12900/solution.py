def solution(n):
    n1, n2 = 1, 2
    n3 = n1 + n2
    for i in range(3, n):
        n1 = n2
        n2 = n3
        n3 = (n1 + n2)%1000000007

    return n3
