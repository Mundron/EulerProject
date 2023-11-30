from datetime import datetime, timedelta

day = timedelta(days=1)

result = 0
current_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)
while current_date <= end_date:
    if current_date.weekday() == 6 and current_date.strftime("%d") == "01":
        result += 1
    current_date += day
print(result)
