# https://www.acmicpc.net/problem/1920

def binary_search(sorted_list, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < x:
            left = mid + 1
        elif sorted_list[mid] > x:
            right = mid - 1
        else:
            return 1
    return 0

n = int(input())
a = [int(x) for x in input().split()]
a.sort()

m = int(input())
b = [int(x) for x in input().split()]

for x in b:
    print(binary_search(a, 0, n - 1, x))
