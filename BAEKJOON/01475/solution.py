n = input()
numbers = [0 for _ in range(10)]
for digit in n:
    numbers[int(digit)] += 1
numbers[6] = (numbers[6] + numbers[9])//2 + (numbers[6] + numbers[9])%2
print(max(numbers[:-1]))
