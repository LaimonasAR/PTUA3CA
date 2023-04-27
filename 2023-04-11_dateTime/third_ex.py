# find next 3 Fridays that happend to be Friday the 13th (classic)

import datetime

today = datetime.datetime.today()

i = 0
while i < 3:
    today = today + datetime.timedelta(days=1)
    # print(today)
    if today.strftime("%A %d") == "Friday 13":
        print(today)
        i += 1
