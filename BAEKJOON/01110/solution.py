import sys
input = sys.__stdin__.readline

n = int(input())
temp = (n%10)*10 + (n//10 + n%10)%10
count = 1
while temp != n:
    temp = (temp%10)*10 + (temp//10 + temp%10)%10
    count += 1

print(count)
