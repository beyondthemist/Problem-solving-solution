import sys
input = sys.__stdin__.readline

def solve(solutions: list[int], n: int) -> str:
    left, right = 0, n - 1

    val = solutions[left] + solutions[right]
    answer = f'{solutions[left]} {solutions[right]}'
    while val != 0:
        if solutions[left] + solutions[right] > 0:
            right -= 1
        elif solutions[left] + solutions[right] < 0:
            left += 1
        
        if left >= right:
            break

        if abs(val) > abs(solutions[left] + solutions[right]):
            val = solutions[left] + solutions[right]
            answer = f'{solutions[left]} {solutions[right]}'

    return answer

n = int(input().rstrip())
solutions = sorted([int(x) for x in input().split()])
print(solve(solutions, n))
