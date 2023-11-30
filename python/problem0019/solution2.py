def next_(day_of_week, year, month, day):
    day_of_week = day_of_week % 7 + 1
    if month in {4, 6, 9, 11}:
        if day < 30:
            day += 1
        else:
            month += 1
            day = 1
    elif month in {1, 3, 5, 7, 8, 10}:
        if day < 31:
            day += 1
        else:
            month += 1
            day = 1
    elif month == 12:
        if day < 31:
            day += 1
        else:
            year += 1
            month = 1
            day = 1
    else:  # february
        leap = (not year % 4) and (year % 100 or not year % 400)
        if (leap and day < 29) or (not leap and day < 28):
            day += 1
        else:
            month = 3
            day = 1

    return day_of_week, year, month, day


result = 0
day_of_week, year, month, day = 1, 1900, 1, 1
while not (year == 2001 and month == 1 and day == 1):
    if day_of_week == 7 and day == 1 and year > 1900:
        result += 1
    day_of_week, year, month, day = next_(day_of_week, year, month, day)

print(result)
