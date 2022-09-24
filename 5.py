day = int(input())
day_of_week = 0

if day == 1:
    day_of_week = 4
elif day == 2:
    day_of_week = 5
elif day == 3:
    day_of_week = 6
else:
    day = day - 3
    day_of_week = day % 7 - 1
print(day_of_week)