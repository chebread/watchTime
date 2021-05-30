# 시계
from datetime import *
def Time():
    _time_ = datetime.now()
    day = _time_.day
    month = _time_.month
    leap_year = LeapYear(_time_.year)
    year = _time_.year
    second = _time_.second
    minute = _time_.minute
    hour = AM(_time_.hour)
    return "%s년 %s월 %s일 %s시 %s분 %s초"%(year, month, day, hour, minute, second)
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
        return "올해는 윤년이에요"
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