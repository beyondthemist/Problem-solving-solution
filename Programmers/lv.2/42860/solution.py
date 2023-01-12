def get_next(name, idx):
    l = len(name)

    f = (idx + 1)%l
    f_cnt = 1
    while f != idx and name[f] == 'A':
        f = (f + 1)%l
        f_cnt += 1

    b = idx - 1
    b_cnt = 1
    while idx - l <= b and name[b] == 'A':
        b -= 1
        b_cnt += 1

    return f, f_cnt, b, b_cnt

def solution(name):
    name = list(name)
    v = min(ord(name[0]) - ord('A'), ord('Z') - ord(name[0]) + 1)
    name[0] = 'A'
    def solve(name=name, cursor=0, c=v):=
        if name.count('A') == len(name):
            return c

        f, f_val, b, b_val = get_next(name=name, idx=cursor)

        f_name = [c for c in name]
        f_val += min(ord(name[f]) - ord('A'), ord('Z') - ord(name[f]) + 1)
        f_name[f] = 'A'
        
        b_name = [c for c in name]
        b_val += min(ord(name[b]) - ord('A'), ord('Z') - ord(name[b]) + 1)
        b_name[b] = 'A'
        
        f_answer = solve(name=f_name, cursor=f, c=c + f_val)
        b_answer = solve(name=b_name, cursor=b, c=c + b_val)

        return min(f_answer, b_answer)
        
    return solve()
