def is_leapYear(year):
    """
    Check if a given year is a leap year.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
def count_days_in_month(year, month):
    """
    Count the number of days in a given month.
    """
    if month < 1 or month > 12:
        return "Invalid month"
    
    # Months with 30 days: April, June, September, November
    # Months with 31 days: January, March, May, July, August, October, December
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leapYear(year):
            return 29
        else:
            return 28
    else:
        return 31
    
year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))
days = count_days_in_month(year, month)
print("Days in %d year %d month is %d days" %(year, month, days))