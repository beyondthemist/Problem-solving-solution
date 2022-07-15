#https://www.acmicpc.net/problem/1003

count = {0:[1, 0], 1:[0, 1]}

inputs = [] # test case T
for i in range(int(input())):
    inputs.append(int(input())) # add input N to list

for j in range(2, max(inputs) + 1):
    count[0].append(count[0][j - 1]  + count[0][j - 2])
    count[1].append(count[1][j - 1]  + count[1][j - 2])

for x in inputs:
    print(count[0][x], count[1][x])
