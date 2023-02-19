def solution(n):
    def solve(b, j=0):
        if j == n - 1:
            return 1

        next = []
        for i in range(n):
            legal = True
            for r in range(0, j + 1):
                if b[j - r] == i - 1 - r \
                or b[j - r] == i \
                or b[j - r] == i + 1 + r:
                    legal = False
                    break

            if legal:
                next.append(i)
        
        if not next:
            return 0
        
        sub_answer = 0
        for nex in next:
            temp = b + [nex]
            sub_answer += solve(b=temp, j=j + 1)
        
        return sub_answer

    answer = 0
    for i in range(n):
        answer += solve(b=[i])
    
    return answer
