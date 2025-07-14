# Calculate the time difference between 1 January 1970 and now.
from datetime import date, datetime
today = date.today()
past = date(year=1970, month=1, day=1)
time_left = today - past
print('Time difference:', time_left)