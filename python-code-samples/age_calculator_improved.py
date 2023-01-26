'''🚀 Age Calculator In Python'''
from datetime import date
import dateutil.relativedelta as rd

today = date.today()
print(f"Today: {today}")

# 👉 Given, Date of Birth
dob = date(year=1995, month=1, day=1)
print(f"DOB: {dob}")

# 👉 Take into account leap years and the difference in months and days also.
diff = rd.relativedelta(today, dob)
print(f"Age: {diff.years} years, {diff.months} months, {diff.days} days")
