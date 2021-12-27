# https://www.acmicpc.net/problem/1924

x = input().split(' ')
y = int(x[1])
x = int(x[0])

monthes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days = {1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT', 0:'SUN'}

today = 0
for month in range(1, x):
     today += monthes[month]

today += y
print(days[today%7])
