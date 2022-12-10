def solution(numbers, target):
    if len(numbers) == 0:
        if target == 0:
            return 1
        else:
            return 0
    else:
        a = solution(numbers[1:], target + numbers[0])
        b = solution(numbers[1:], target - numbers[0])
        return a + b
