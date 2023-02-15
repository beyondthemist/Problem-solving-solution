import sys
input = sys.__stdin__.readline

print('SK' if int(input()) & 1 else 'CY')
