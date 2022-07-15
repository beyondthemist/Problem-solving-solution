# https://www.acmicpc.net/problem/1920

def binary_search(sorted_list, left, right, x):
    if left > right:
        return 0
    
    mid = (left + right) // 2
    
    if sorted_list[mid] < x:
        return binary_search(sorted_list, mid + 1, right, x)
    elif sorted_list[mid] > x:
        return binary_search(sorted_list, left, mid - 1, x)
    else:
        return 1

n = int(input())
a = [int(x) for x in input().split()]
a.sort()

m = int(input())
b = [int(x) for x in input().split()]

for x in b:
    print(binary_search(a, 0, n - 1, x))
