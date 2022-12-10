def solution(numbers, target):
    l = len(numbers)
    
    def solve(s=0, i=0):
        if i == l:
            return int(s == target)
        
        a = solve(s=s + numbers[i], i=i + 1)
        b = solve(s=s - numbers[i], i=i + 1)
    
        return a + b

    return solve()
