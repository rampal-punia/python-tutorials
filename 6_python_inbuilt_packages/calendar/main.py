'''📝 Example codes used in readme.md

✨ Run and check the output
'''

import calendar

# Weekdays numbering

print(calendar.MONDAY)
print(calendar.TUESDAY)
print(calendar.WEDNESDAY)
print(calendar.THURSDAY)
print(calendar.FRIDAY)
print(calendar.SATURDAY)
print(calendar.SUNDAY)


# Set the start of the weekday
calendar.setfirstweekday(6)

# Or
calendar.setfirstweekday(calendar.MONDAY)


# iterweekdays
cal = calendar.Calendar()
for weekday in cal.iterweekdays():
    print(weekday)
for month_dates in cal.itermonthdates(year=2022, month=2):
    print(month_dates)
for month_day in cal.itermonthdays(year=2022, month=3):
    print(month_day)

# Print calendar
calendar.setfirstweekday(0)
print(calendar.calendar(theyear=2023, m=4))
