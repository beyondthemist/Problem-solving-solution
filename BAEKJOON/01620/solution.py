import sys
input = sys.__stdin__.readline

n, m = [int(x) for x in input().split()]
pokemon_dict = {}
index_dict = {}
for idx in range(1, n + 1):
    pokemon = input().rstrip()
    pokemon_dict[idx] = pokemon
    index_dict[pokemon] = idx

for _ in range(m):
    answer = input().rstrip()

    if answer.isalpha():
        print(index_dict[answer])
    else:
        print(pokemon_dict[int(answer)])
