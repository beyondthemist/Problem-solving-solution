from typing import List, Set

def solution(k: int, dungeons: List[int]):
    n = len(dungeons)

    def explore(curr_hp=k, curr_stage=0, explored: Set[int]=set()) -> int:
        # Look out dungeons to explore
        to_explore = list()
        for i in range(n):
            if curr_hp >= dungeons[i][0] \
                and i not in explored:
                to_explore.append(i)

        # base case
        # if no dungeon to explore then end the exploratory
        if not to_explore:
            return curr_stage

        res = -1
        for dest_idx in to_explore:
            x = explore(
                curr_hp=curr_hp - dungeons[dest_idx][1],
                curr_stage=curr_stage + 1,
                explored=explored.union(set([dest_idx]))
            )
            if res < x:
                res = x

        return res

    return explore()
