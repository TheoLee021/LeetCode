# Calculating New Date Given Number of Days
def add_days(date, n):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    y, m, d = map(int, date.split("-"))
    
    def is_leap_year(year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False
    
    def dim(y, m):
        return 29 if is_leap_year(y) and m == 2 else days_in_month[m]

    # Adding days from month 1
    monthDays = 0
    for i in range(1, m):
        monthDays += dim(y, i)
    
    # Calculate total days
    totalDays = monthDays + (d - 1) + n
    
    # Convert total days to YYYY-MM-DD
    # Count year considering leap year
    year = y
    while True:
        days_this_year = 366 if is_leap_year(year) else 365
        if totalDays < days_this_year:
            break
        totalDays -= days_this_year
        year += 1
    
    # Count months considering leap month
    month = 1
    while True:
        days_this_month = dim(year, month) # replace to dim()
        if totalDays < days_this_month:
            break
        totalDays -= days_this_month
        month += 1
    
    day = totalDays + 1
    
    return f"{year:04d}-{month:02d}-{day:02d}"