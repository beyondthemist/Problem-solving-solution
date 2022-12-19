import sys
input = sys.__stdin__.readline

def solve(a: list[int], n):
    left, right = 0, n - 1

    val = a[left] + a[right]
    answer = f'{a[left]} {a[right]}'
    while val != 0:
        if a[left] + a[right] > 0:
            right -= 1
        elif a[left] + a[right] < 0:
            left += 1
        
        if left >= right:
            break

        if abs(val) > abs(a[left] + a[right]):
            val = a[left] + a[right]
            answer = f'{a[left]} {a[right]}'

    return answer

n = int(input().rstrip())
a = sorted([int(x) for x in input().split()])
print(solve(a, n))
