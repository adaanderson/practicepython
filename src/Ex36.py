import bokeh
import json
from collections import Counter
from datetime import datetime
from bokeh.plotting import figure, show, output_file

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

dates = []

for value in birthdays.values():
    format_str = '%m/%d/%Y'  
    datetime_obj = datetime.strptime(value, format_str)  
    res = datetime_obj.strftime("%b")
    dates.append(res)

sorted_dates = Counter(dates)
print(sorted_dates)

output_file("plot.html")
x_categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
x = list(sorted_dates.keys())
y = list(sorted_dates.values())

p = figure(x_range=x_categories)

p.vbar(x=x, top=y, width=0.5)

show(p)