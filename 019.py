# Project Euler
# Problem 18 
#
# Counting Sundays

def next_day(current):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  for idx, day in enumerate(days):
    if current == day:
      if idx == 6:
        return days[0]
      else:
        return days[idx + 1]

def next_month(current):
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  for idx, month in enumerate(months):
    if current == month:
      if idx == 11:
        return months[0]
      else:
        return months[idx + 1]

def month_days(month, year):
  days = {}
  days['January']   = 31
  days['February']  = 28
  days['March']     = 31
  days['April']     = 30
  days['May']       = 31
  days['June']      = 30
  days['July']      = 31
  days['August']    = 31
  days['September'] = 30
  days['October']   = 31
  days['November']  = 30
  days['December']  = 31
  if year % 4 == 0:
    if (year % 400 == 0) or (year % 100 != 0):
      days['February'] = 29
  return days[month]

if __name__ == "__main__":
  day = 1
  month = 'January'
  year = 1901
  day_name = 'Monday'
  count = 0

  while year < 2000:
    for d in range(1,month_days(month, year) + 1):
      day = d
      if day == 1 and day_name == 'Sunday': count += 1
      day_name = next_day(day_name)
    month = next_month(month)
    if month == 'January': year += 1

print count
