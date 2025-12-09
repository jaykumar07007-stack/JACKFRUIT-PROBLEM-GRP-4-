from datetime import date

def get_event_date():#this is for getting valid date if wrong raises error if i enter jan 52 
        try:
            event_year = int(input("Enter Year: "))
            event_month = int(input("Enter Month (1-12): "))
            event_day = int(input("Enter Day number (e.g. 1-31): "))
            return date(event_year, event_month, event_day)
        except ValueError:
            print("Invalid date! Please enter a valid day, month, and year.")
            exit()

def countdown(event_date, event_name):#event date is say(2025,12,29) 
    today = date.today()#todays date say(2025,12,7)
    time_diff = event_date - today# this gives days differnce here 12days
    number_of_days = time_diff.days# this for getting or extracting days here 12
    if number_of_days < 0:
        print("Sorry, the event is closed.")
    elif number_of_days == 0:
        print(f"Hurry up! The {event_name} is today!")
    else:
        years = number_of_days // 365 # gives year for ex 366 days mean 1 year 
        months = (number_of_days % 365) // 30 # gives month 
        days = (number_of_days % 365) % 30 
        print(f"The {event_name} starts in {years} years, {months} months, and {days} days.")
event_name = input("Enter the name of the event: ")
event_date = get_event_date()#calling function and storing ex(2025,4,4)
print("Today's Date:", date.today())
countdown(event_date, event_name)