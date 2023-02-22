from collections import deque

def solution(maps):
    maps = [list(map) for map in maps]
    src, lever, exit = (), (), ()
    rows = len(maps)
    cols = len(maps[0])
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                src = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
    
    def solve(src, dest, rows=rows, cols=cols):
        val = 0
        q = deque()
        q.append((src[0], src[1], val))
        ans = ()
        visited = set()
        visited.add((src[0], src[1]))
        
        d = [-1, 1, 0, 0]
        while q:
            v = q.popleft()
            val = v[-1]
            if (v[0], v[1]) == dest:
                ans = v
                break
            
            for i in range(len(d)):
                x, y = v[0] + d[i], v[1] + d[-(i + 1)]
                
                if (0 <= x and x < rows) \
                and (0 <= y and y < cols) \
                and maps[x][y] != 'X' \
                and (x, y) not in visited:
                    q.append((x, y, val + 1))
                    visited.add((x, y))
    
        return ans[-1] if ans else -1

    ans1 = solve(src=src, dest=lever)
    ans2 = 0
    if ans1 != -1:
        ans2 = solve(src=lever, dest=exit)

    answer = ans1 + ans2
    return answer if ans1 != -1 and ans2 != -1 else -1
