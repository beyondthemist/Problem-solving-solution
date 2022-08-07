from typing import List

def binary_search(sorted_list: List, left: int, right: int, x: int) -> bool:
    while left <= right:
        mid: int = (left + right) // 2
        
        if sorted_list[mid] < x:
            left = mid + 1
        elif sorted_list[mid] > x:
            right = mid - 1
        else:
            return True
    
    return False

n = int(input())
cards = [int(x) for x in input().strip().split()]
m = int(input())
to_find = [int(y) for y in input().strip().split()]
sorted_to_find = sorted(to_find)
cnt = {k: 0 for k in to_find}

for card in cards:
    if binary_search(sorted_to_find, 0, m - 1, card):
        cnt[card] += 1

print(' '.join([str(cnt[k]) for k in to_find]))
