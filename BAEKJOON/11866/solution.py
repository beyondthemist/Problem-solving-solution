import sys 
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]
numbers = list(range(1, n + 1))
answer = []

idx = 0
while numbers:
    idx = (idx + (k - 1))%len(numbers)
    answer.append(str(numbers.pop(idx)))

print(f"<{', '.join(answer)}>")
