import datetime
#Write a function that calculates difference in days between two datetimes. 

def calculate_days():
    y = datetime.datetime(2000, 2, 29, 18, 20, 50)
    x = datetime.datetime.today()
    z = x - y
#print(z)
    print(z.days)
calculate_days()