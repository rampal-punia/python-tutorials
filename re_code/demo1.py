import re

message = "Call me at 489-555-1111 at noon. 489-555-9999 is my office"
phone_number = re.sub(r"\D", "", message)
print(phone_number[:10], phone_number[11:])
