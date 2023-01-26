'''🚀 Age Calculator In Python'''
from datetime import date
import dateutil.relativedelta as rd

year_of_birth = 1995
month_of_birth = 1
day_of_birth = 1

today = date.today()
print(f"Today: {today}")

# 👉 Given, Date of Birth
dob = date(year_of_birth, month_of_birth, day_of_birth)
print(f"DOB: {dob}")

# 👉 Take into account leap years and the difference in months and days also.
diff = rd.relativedelta(today, dob)
print(f"Age: {diff.years} years, {diff.months} months, {diff.days} days")
