import sys
input = sys.__stdin__.readline

def dfs(m, i, j, n, count=0, val=2) -> int:
    d = [-1, 1, 0, 0]
    visited = set()
    queue = [(i, j)]

    while queue:
        v = queue.pop(0)
        i, j = v[0], v[1]

        if v not in visited:
            visited.add(v)
            m[i][j] = val
            count += 1

            for idx in range(len(d)):
                new_i = i + d[idx]
                new_j = j + d[-(idx + 1)]
                if (0 <= new_i and new_i < n) \
                and (0 <= new_j and new_j < n):
                    if m[new_i][new_j] == 1:
                        queue.append((new_i, new_j))
    return count

n = int(input())
m = [[int(c) for c in list(input().strip())] for _ in range(n)]
ans = []
val = 2
for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            cnt = dfs(m=m, i=i, j=j, n=n, val=val)
            ans.append(cnt)
            val += 1

ans.sort()
print(len(ans))
print('\n'.join(map(str, ans)))
