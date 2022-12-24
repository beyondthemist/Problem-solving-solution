def get_latest_idx(appliances, appliance, idx, k):
    n = idx
    while n < k and appliances[n] != appliance: n += 1

    return n


def solve(n, k, appliances):
    if n == 1:
        cnt = 0
        for i in range(1, k):
            if appliances[i] != appliances[i - 1]:
                cnt += 1
        return cnt

    power_bar = set()
    cnt = 0
    for i in range(k):
        if len(power_bar) < n:
            power_bar.add(appliances[i])
            continue
        
        if appliances[i] not in power_bar:
            temp = set(appliances[i + 1:])
            to_unplug = -1
            for s in power_bar:
                if s not in temp:
                    to_unplug = s
                    break
            
            if to_unplug == -1:
                idx_to_unplug = i
                for appliance in power_bar:
                    t = get_latest_idx(appliances, appliance, i + 1, k)
                    if idx_to_unplug < t:
                        idx_to_unplug = t
                to_unplug = appliances[idx_to_unplug]

            power_bar.remove(to_unplug)
            cnt += 1
            power_bar.add(appliances[i])

    return cnt

n, k = [int(x) for x in input().split()]
appliances = [int(x) for x in input().split()]

print(solve(n, k, appliances))
