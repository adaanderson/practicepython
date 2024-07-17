import json
from collections import Counter
from datetime import datetime

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

dates = []

for value in birthdays.values():
    format_str = '%m/%d/%Y'  
    datetime_obj = datetime.strptime(value, format_str)  
    res = datetime_obj.strftime("%B")
    dates.append(res)

sorted_dates = Counter(dates)
print(sorted_dates)