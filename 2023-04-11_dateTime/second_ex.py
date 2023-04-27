# Write a function that takes a datetime object, which will represent employees starting work day. and will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off
import datetime

y = datetime.date(2020, 1, 1)
x = datetime.date.today()

# print(z)
diff = (x.year - y.year) * 12 + (x.month - y.month)

holidays = diff * 1.6

print(round(holidays))
