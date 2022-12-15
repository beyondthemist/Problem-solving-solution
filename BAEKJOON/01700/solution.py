def rindex(ss, s, idx, k):
    n = idx
    while n < k and ss[n] != s: n += 1

    return n


def solve(n, k, ss: list[int]):
    if n == 1:
        cnt = 0
        for i in range(1, k):
            if ss[i] != ss[i - 1]:
                cnt += 1
        return cnt

    power_bar = set()
    cnt = 0
    for i in range(k):
        if len(power_bar) < n:
            power_bar.add(ss[i])
            continue
        
        if ss[i] not in power_bar:
            # 안 쓰는 거
            temp = set(ss[i + 1:])
            val = -1
            for s in power_bar:
                if s not in temp:
                    val = s
                    break
            
            if val == -1: # 안 쓰는 게 없음 -> 다음 사용까지 시간이 가장 긴 거
                ridx = i
                for s in power_bar:
                    t = rindex(ss, s, i + 1, k)
                    if ridx < t:
                        ridx = t
                val = ss[ridx]
            power_bar.remove(val)
            cnt += 1
            power_bar.add(ss[i])


    return cnt

n, k = [int(x) for x in input().split()]
ss = [int(x) for x in input().split()]

print(solve(n, k, ss))
