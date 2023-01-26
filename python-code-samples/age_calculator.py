'''✨ Age Calculator In Python.✨'''
from datetime import date
year_of_birth = 1995
month_of_birth = 1
day_of_birth = 1

today = date.today()
print(f"Today: {today}")

# 👉 Given, Date of Birth
dob = date(year_of_birth, month_of_birth, day_of_birth)
print(f"DOB: {dob}")

# 👉 Days till today
total_days = (today-dob).days
print(f"Days: {total_days}")

# 👉 Years till today
years = total_days/365
print(f"In Years: {years:.2f}")

# Note: This does not take into account the leap year.
