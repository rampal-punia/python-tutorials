import time

localtime = time.ctime()
print(localtime)
# Output: Fri Nov  4 21:33:46 2022

str_format_time = time.strftime("%Y: %m : %d ")
print(str_format_time)
# 2022: 11 : 04

"""
Convert a time tuple to a string according to a format specification.
Common formats:
%Y = Year with century
%m = Month [01, 12]
%d = Day of the month [01, 31]
%H = Hour(24-hour clock) [00, 23]
%M = Minute [00, 59]
%S = Second[00, 61] Yup!!! The range for seconds really is 0 to 61; 
according to the Posix standard this accounts for leap seconds and 
the (very rare) double leap seconds. The time module may produce 
and does accept leap seconds since it is based on the Posix standard.
%z = Time zone offset from UTC.
And more... (refer docs) 
"""

current_time_in_secs = time.time()
print(current_time_in_secs)
