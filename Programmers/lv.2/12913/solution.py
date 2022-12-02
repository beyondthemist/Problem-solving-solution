from typing import List

def solution(land: List[List[int]]) -> int:
    rows = len(land)
    cols = 4 #len(land[0])

    dp = [[0 for j in range(cols)] for i in range(rows)]
    dp[0] = list(land[0])
    for i in range(1, rows):
        # generalized
        for j in range(cols):
            prev_scores = []
            for k in range(cols):
                if k != j:
                    prev_scores.append(dp[i - 1][k])
            dp[i][j] = land[i][j] + max(prev_scores)

        # specilaized for this problem
        #dp[i][0] = land[i][0] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3])
        #dp[i][1] = land[i][1] + max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3])
        #dp[i][2] = land[i][2] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3])
        #dp[i][3] = land[i][3] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])

    answer = max(dp[-1])
    return answer

#print(solution(land=[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
#print(solution(land=[[1, 1, 1, 1], [2, 2, 2, 3], [3, 3, 3, 6], [4, 4, 4, 7]]))
#print(solution(land=[[9, 5, 2, 3], [9, 8, 6, 7], [8, 9, 7, 1], [100, 9, 8, 1]]))
