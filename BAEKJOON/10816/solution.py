import sys

input = sys.stdin.readline

n = int(input())
cards = [int(x) for x in input().strip().split()]

m = int(input())
to_find = [int(y) for y in input().strip().split()]

cnt = {k: 0 for k in to_find}

for card in cards:
    if cnt.get(card) != None:
        cnt[card] += 1

print(' '.join([str(cnt[k]) for k in to_find]))
