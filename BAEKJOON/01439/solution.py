import sys 
input = sys.stdin.readline

s = input().rstrip()
print(max(s.count('01'), s.count('10')))
