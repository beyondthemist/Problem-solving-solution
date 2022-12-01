# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from typing import Set

def solution(k, dungeons):
    n = len(dungeons)

    def discover(curr_hp=k, discovered_stage=0, discovered: Set[int]=set()) -> int:
        # if all dungeons are discovered
        if discovered_stage >= n:
            return n

        # Look out dungeon to discover
        to_discover = list()
        for i in range(n):
            if curr_hp >= dungeons[i][0] \
                and i not in discovered:
                to_discover.append(i)
        
        # if there is no dungeon to discover
        if not to_discover:
            return discovered_stage


        # if there is dungeon to discover
        res = -1
        for dest_idx in to_discover:
            x = discover(
                curr_hp=curr_hp - dungeons[dest_idx][1],
                discovered_stage=discovered_stage + 1,
                discovered=discovered.union(set([dest_idx]))
            )

            if res < x:
                res = x

        return res

    return discover()

# print(solution(80, [[80, 20], [50, 40], [700, 10]])) -> 2
# print(solution(80, [[80, 20], [50, 40], [70, 10]])) -> 2
