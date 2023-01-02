from collections import deque

def solution(maps):
    n, m = len(maps[0]), len(maps)

    def bfs(n=n, m=m, visited=set()):
        d = [-1, 1, 0, 0]
        visited.add((0, 0))
        to_visit = deque([(0, 0, 1)])
        while to_visit:
            i, j, c = to_visit.popleft()

            for idx in range(4):
                next_i, next_j = (i + d[idx], j + d[-(idx + 1)])
                next = (next_i, next_j)

                if next_i  == m - 1 and next_j == n - 1:
                    return c + 1

                if next not in visited \
                and (0 <= next_i and next_i < m) \
                and (0 <= next_j and next_j < n) \
                and maps[next_i][next_j] == 1:
                    to_visit.append((next_i, next_j, c + 1))
                    visited.add(next)

        return -1

    return bfs()
