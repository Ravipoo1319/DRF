import datetime

date_time_string = "Jan 1 2014 2:43PM"

date_time_obj = datetime.datetime.strptime(date_time_string,"%b %d %Y %I:%M%p")

print(date_time_obj)