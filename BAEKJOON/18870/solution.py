def solution():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    sorted_unique = sorted(list(set(numbers)))
    d = {t[1]: t[0] for t in enumerate(sorted_unique, 0)}
    answer = [str(d[x]) for x in numbers]
    
    return ' '.join(answer)

print(solution())
