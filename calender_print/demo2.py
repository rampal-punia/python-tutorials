import calendar

print(calendar.SUNDAY)
print(calendar.MONDAY)
print(calendar.TUESDAY)

calendar.setfirstweekday(0)
print(calendar.calendar(theyear=2023, m=4))
