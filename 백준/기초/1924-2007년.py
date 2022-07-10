x,y = map(int, input().split())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
date = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

day=0
for i in range(x-1):
    day+=month[i]
day+=y

print(date[day%7])