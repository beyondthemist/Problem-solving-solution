import sys
input = sys.__stdin__.readline

from typing import List


def binary_search(trees: List[int]) -> int:
    s = 0
    left, right = 1, sum(trees)
    while left <= right:
        mid = (left + right) // 2
        s = sum([tree - min(tree, mid) for tree in trees])

        if s >= m:
            left = mid + 1
        else:
            right = mid - 1

    return right

n, m = list(map(int, input().split()))
h: List[int] = sorted(list(map(int, input().split())))

print(binary_search(h))
