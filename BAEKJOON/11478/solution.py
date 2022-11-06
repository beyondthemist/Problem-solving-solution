s = input()
subsets = set()
for i in range(len(s)):
    for j in range(len(s) - i):
        subsets.add(s[j:j + i + 1])

print(len(subsets))
