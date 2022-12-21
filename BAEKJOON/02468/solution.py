import sys
input = sys.__stdin__.readline

from collections import deque

def solve(arr: list[list[int]], n: int) -> int:
    def bfs(
        root: tuple[int, int],
        height: int,
        visited: set[tuple[int, int]],
    ) -> list[int, set[int]]:
        if root in visited \
        or arr[root[0]][root[1]] <= height:
            return 0
        
        d: deque[tuple[int, int]] = deque()

        visited.add(root)
        d.append(root)
        while d:
            v: tuple[int, int] = d.popleft()
            offsets: list[int] = [-1, 1, 0, 0]
            for idx in len(offsets):
                i, j = v[0] + offsets[idx], v[1] + offsets[-(idx + 1)]
                
                if 0 <= i and i < n \
                and 0 <= j and j < n  \
                and (i, j) not in visited \
                and arr[i][j] > height:
                    d.append((i, j))
                    visited.add(v)

        return 1


    heights: set[int] = set()
    for row in arr:
        heights = heights.union(set(row))
    heights.add(min(heights) - 1)

    visited: set[tuple[int, int]] = set()
    answer = -1
    for height in heights:
        # count safe area
        cnt = 0

        # search
        visited.clear()
        for i in range(n):
            for j in range(n):
                cnt += bfs(root=(i, j), height=height, visited=visited)
    
        # get max
        if answer < cnt:
            answer = cnt

    return answer


n = int(input().rstrip())
arr = [[int(x) for x in input().split()] for _ in range(n)]

print(solve(arr, n))
