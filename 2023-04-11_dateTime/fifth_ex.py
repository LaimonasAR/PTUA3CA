# Write a Python program to get the last day of a specified year and month, Example: Monday, Tuesday etc.

import datetime


def last_day_of_month(date: datetime.date) -> None:
    date_for_calculations = date
    while date.month == date_for_calculations.month:
        date_for_calculations = date_for_calculations + datetime.timedelta(days=1)
        # print(date_for_calculations)
        if date.month != date_for_calculations.month:
            date_for_calculations = date_for_calculations - datetime.timedelta(days=1)
            print(date_for_calculations.day)
            break


date = datetime.date(2023, 2, 25)

last_day_of_month(date=date)
