import sys
input = sys.__stdin__.readline

from typing import Tuple, List, Set


def dfs(
    board: List[List[int]],
    src_i: int,
    src_j: int,
    dest_i: int,
    dest_j: int,
    n: int
) -> bool:
    queue: List[Tuple[int]] = [(src_i, src_j)]
    visited: Set[int] = set()
    di_list = [-2, -1, 1, 2, 2, 1, -1, -2]
    dj_list = [1, 2, 2, 1, -1, -2, -2, -1]
    i, j = 0, 0
    
    while queue:
        v = queue.pop(0)
        i, j = v[0], v[1]

        if i == dest_i and j == dest_j:
            return board[i][j] - 1

        for di, dj in zip(di_list, dj_list):
            new_i, new_j = i + di, j + dj

            if (0 <= new_i and new_i < n) \
            and (0 <= new_j and new_j < n):
                if board[new_i][new_j] != 1:
                    board[new_i][new_j] = board[i][j] + 1
                    new_v = (new_i, new_j)
                    
                    if new_v not in visited:
                        queue.append(new_v)
                        visited.add(new_v)

    return 0

t = int(input())
for _ in range(t):
    l = int(input())
    board = [[0 for j in range(l)] for i in range(l)]
    src_i, src_j = map(int, input().split())
    dest_i, dest_j = map(int, input().split())
    board[src_i][src_j] = 1 #sentinel
    print(dfs(board, src_i, src_j, dest_i, dest_j, l))
    
