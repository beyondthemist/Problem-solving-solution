import sys
input = sys.__stdin__.readline

def solution(n: int) -> int:
    def solve(b: list[int], j: int=0) -> int:
        if j == n - 1:
            return 1
        # add legal index
        next = []
        for i in range(n): # when b[j + 1] == i
            legal = True
            for r in range(0, j + 1):
                if b[j - r] == i - 1 - r \
                or b[j - r] == i \
                or b[j - r] == i + 1 + r:
                    legal = False

                if not legal:
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

n = int(input())
print(solution(n=n))
