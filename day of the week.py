import datetime
import calendar  

day = int(input("Enter the date (day number, e.g. 1–31): "))
month = int(input("Enter the month number (e.g. 1–12): "))
year = int(input("Enter the year (e.g. 2025): "))

leap = calendar.isleap(year)


if month == 2:
    if leap and day > 29:
        print("Invalid date! February has only 29 days in a leap year.")
        exit()
    elif not leap and day > 28:
        print("Invalid date! February has only 28 days.")
        exit()

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if month != 2 and day > month_days[month]:
    print("Invalid date!")
    exit()


date = datetime.date(year, month, day)
print("Day of the week is:", date.strftime("%A"))