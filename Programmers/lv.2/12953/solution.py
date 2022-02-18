# https://programmers.co.kr/learn/courses/30/lessons/12953

def gcd(a, b):
    return (b if a%b == 0 else gcd(b, a%b)) if a > b else (a if b%a == 0 else gcd(a, b%a))

def lcm(arr, n):
    val = lcm(arr[1:], arr[0]) if len(arr) > 1 else arr[0]
    return (val * n) // gcd(val, n)

def solution(arr):
    return lcm(arr[1:], arr[0])
