import datetime

current_year = datetime.date.today().strftime("%Y")

rem = int(current_year) % 4

if rem == 0:
    print("IT IS LEAP YEAR")
else:
    print("IT IS NOT A LEAP YEAR")