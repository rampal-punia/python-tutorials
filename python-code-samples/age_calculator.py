'''🚀 Age Calculator In Python'''
from datetime import date

today = date.today()
print(f"Today: {today}")

# 👉 Given, Date of Birth
dob = date(year=1995, month=1, day=1)
print(f"DOB: {dob}")

# 👉 Days till today
total_days = (today-dob).days
print(f"Days: {total_days}")

# 👉 Years till today
years = total_days/365
print(f"In Years: {years:.2f}")
