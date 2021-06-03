# Watch
from datetime import *
def Time():
    _time_ = datetime.now()
    day = _time_.day
    month_num = _time_.month
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = months[month_num]
    leap_year = LeapYear(_time_.year)
    weekdays = ['Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun']
    weekday_num = _time_.today().weekday()
    weekday = weekdays[weekday_num]
    year = _time_.year
    second = _time_.second
    minute = _time_.minute
    hour = AM(_time_.hour)
    return "%s %s %s %s:%s:%s %s"%(weekday,  month, day, hour, minute, second, year)
def AM(hour):
    if hour > 12:
        am = hour - 12
        return am
    else:
        return hour
def LeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    else:
        return -1
def DisplayLeapYear(n):
    if n == -1:
        return "This year a leap year"
    else:
        pass
watch = Time()
print("Watch")
_time_ = datetime.now()
if LeapYear(_time_.year) == 1:
    print(DisplayLeapYear(LeapYear(_time_.year)))
else:
    pass
print(watch)
