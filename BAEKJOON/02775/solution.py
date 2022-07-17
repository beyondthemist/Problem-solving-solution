t = int(input())
d = {'k': [], 'n': []}
for i in range(t):
    d['k'].append(int(input()))
    d['n'].append(int(input()))

''' construct apart '''
# maximum of floor and room number
max_k = max(d['k'])
max_n = max(d['n'])
a = [list(range(1, max_n + 1))] 
for i in range(max_k): # sentinel to construct apart
    a[i][0] = 1                                  # Only one person 
    a.append([1] + [0 for j in range(1, max_n)]) # in room XX1
for i in range(1, max_k + 1): # DP
    for j in range(1, max_n):
        a[i][j] = sum(a[i - 1][:(j + 1)])

'''print answer'''
for i in range(t):
    print(a[d['k'][i]][d['n'][i] - 1]) #room number
