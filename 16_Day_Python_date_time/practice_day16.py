# Get the current day, month, year, hour, minute and timestamp from datetime module:
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute, timestamp)
print('timestamp', timestamp)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S"):
from datetime import datetime
now = datetime.now()
time = now.strftime("%m/%d/%Y, %H:%M:%S")
print('time:', time)

# Today is 5 December, 2019. Change this time string to time:
from datetime import datetime
today = "5 December, 2019"
date_object = datetime.strptime(today, "%d %B, %Y")
print(date_object)

# Calculate the time difference between now and new year:
from datetime import date, datetime
dir(date)
help(date)
help(datetime)

today = date.today()
new_year = date(year=2026, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)


# Calculate the time difference between 1 January 1970 and now.
from datetime import date, datetime
today = date.today()
past = date(year=1970, month=1, day=1)
time_left = today - past
print('Time difference:', time_left)

