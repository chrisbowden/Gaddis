# This is a time calculator
# User enters a number of seconds
# and we display how many minutes, hours and days

seconds = int(input("Enter the number of seconds: "))

if seconds >= 60:
    minutes = seconds // 60
    print(minutes, "Minutes")

if seconds >= 3600:
    hours = seconds // 3600
    print(hours, "Hours")

if seconds >= 86400:
    days = seconds // 86400
    print(days, "Days")