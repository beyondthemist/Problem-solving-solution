import sys
input = sys.__stdin__.readline

n = int(input())
pattern = ('CY', 'SK', 'CY', 'SK', 'SK', 'SK', 'SK')

if n == 0:
    print('SK')
else:
    print(pattern(n%7))
