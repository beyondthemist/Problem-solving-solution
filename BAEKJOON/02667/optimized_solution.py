import sys
input = sys.__stdin__.readline

from typing import List, Set, Tuple


def dfs(m: List[List[int]], i: int, j: int, n: int, count: int=0) -> int:
    d: List[int] = [-1, 1, 0, 0]
    visited: Set[int] = set()
    queue: List[Tuple[int, int]] = [(i, j)]

    while queue:
        v: Tuple[int] = queue.pop(0)
        i: int = v[0]
        j: int = v[1]

        if v not in visited:
            visited.add(v)
            m[i][j] = 2
            count += 1

            for idx in range(len(d)):
                new_i: int = i + d[idx]
                new_j: int = j + d[-(idx + 1)]
                if (0 <= new_i and new_i < n) \
                and (0 <= new_j and new_j < n):
                    if m[new_i][new_j] == 1:
                        queue.append((new_i, new_j))

    return count

n: int = int(input())
m: List[List[int]] = [[int(c) for c in list(input().strip())] for _ in range(n)]
ans: List[int] = []
for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            ans.append(dfs(m=m, i=i, j=j, n=n))

ans.sort()
print(len(ans), '\n'.join(map(str, ans)), sep='\n')
