def check_leap_year(yr):
    if (yr % 4) == 0:
        if (yr % 100) == 0:
            if (yr % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


yr = int(input("Enter a year:"))

if (check_leap_year(yr)):
    print("This is a leap year.")
else:
    print("This is not a leap year.")