n, m = [int(x) for x in input().split()]
no_heard = set([input() for _ in range(n)])
no_seen = set([input() for _ in range(m)])
no_heard_seen = sorted(list(no_heard.intersection(no_seen)))

print(len(no_heard_seen), '\n'.join(no_heard_seen), sep='\n')
