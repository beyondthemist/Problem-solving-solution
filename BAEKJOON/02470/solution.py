import sys
input = sys.__stdin__.readline

def solve(solutions: list[int], n: int) -> str:
    left, right = 0, n - 1

    val = solutions[left] + solutions[right]
    answer = f'{solutions[left]} {solutions[right]}'
    while val != 0:
        new_val = solutions[left] + solutions[right]
        if new_val > 0:
            right -= 1
        elif new_val < 0:
            left += 1
        
        if left >= right:
            break

        if abs(val) > abs(new_val):
            val = new_val
            answer = f'{solutions[left]} {solutions[right]}'

    return answer

n = int(input().rstrip())
solutions = sorted([int(x) for x in input().split()])
print(solve(solutions, n))
