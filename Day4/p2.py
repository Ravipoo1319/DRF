# 1. Write a Python script to display the various Date Time formats?

# a) Current date and time :
import datetime

cureent_date_and_time = datetime.datetime.now()

print("current date and time :",cureent_date_and_time)

print("Current Date :", cureent_date_and_time.date())

print("Current Time :",cureent_date_and_time.time())

# Current Year
today = datetime.date.today()
print("Current Year :",today.year)
print("Current Month :",today.month)
print("Current day :",today.day)