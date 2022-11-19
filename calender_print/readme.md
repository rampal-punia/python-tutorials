# Calendar Module of Python

`Calendar` is an in-built Python package to provide useful functions related to calendar.

## Week Day Numbers
```python
print(calendar.MONDAY)      # Output: 0
print(calendar.TUESDAY)     # Output: 1
print(calendar.WEDNESDAY)   # Output: 2
print(calendar.THURSDAY)    # Output: 3
print(calendar.FRIDAY)      # Output: 4
print(calendar.SATURDAY)    # Output: 5
print(calendar.SUNDAY)      # Output: 6
```

## setfirstweekday()
By default, these calendars have Monday as the first day of the week, and Sunday as the last. We can set the first day using setfirstweekday().

```python
# Set the start of the weekday
calendar.setfirstweekday(6)

# Or
calendar.setfirstweekday(calendar.SUNDAY)
```

## Print calendar for the year

```python
# Print calendar
calendar.setfirstweekday(0)
print(calendar.calendar(theyear=2023, m=4))
```

