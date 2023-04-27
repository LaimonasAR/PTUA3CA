# Write a python function that takes nothing but returns the datetime object of last Friday

import datetime


def last_friday():
    today = datetime.datetime.today()

    i = 0
    while i < 1:
        today = today - datetime.timedelta(days=1)
        # print(today)
        if today.strftime("%A") == "Friday":
            print(today)
            i += 1


last_friday()
