import calendar
def show_calendar():
    try:
        year=int(input("Enter the year:"))
        month=int(input("Enter the month in numbers:"))
        print("CALENDAR")
        print(calendar.month(year,month))
    except ValueError:
        print("Please enter valid integers for year and month.")

if __name__=="__main__":
    show_calendar()