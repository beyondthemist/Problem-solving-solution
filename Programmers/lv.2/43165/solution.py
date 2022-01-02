https://programmers.co.kr/learn/courses/30/lessons/43165

def solve(numbers, target, idx, count):
    if idx >= len(numbers): # base case
        return 1 if sum(numbers) == target else 0

    temp = [x for x in numbers]
    temp[idx] = -temp[idx]

    a = solve(temp, target, idx + 1, count)
    b = solve(numbers, target, idx + 1, count)
    
    return a + b

def solution(numbers, target):
    return solve(numbers, target, 0, 0)
