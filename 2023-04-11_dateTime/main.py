# import datetime

# x = datetime.datetime.today()
# print(x)

# print(x.strftime("%B %d, %A, %X, %U week"))

# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, "lt_LT.UTF-8")
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))

# import datetime

# now = datetime.datetime.now()
# # print(now)
# # print(now - datetime.timedelta(days=5))
# # print(now + datetime.timedelta(hours=5))
# # print(now + datetime.timedelta(days=20, hours=8))

# y = datetime.datetime(2000, 2, 29, 18, 20, 50)
# x = datetime.datetime.today()
# z = x - y
# print(z)

# print(z.days)

import datetime

x = datetime.datetime.today()

print(x)
print(x - datetime.timedelta(days=5))
print(x - datetime.timedelta(hours=8))
print(x.strftime("%Y %m %d, %X"))
