# 한글 시계
from datetime import *
print("-- 한글 시계 --")
clock = datetime.now() # Flame
year = clock.year
def koTime(n):
    if n == 1:
        return "한"
    elif n == 2:
        return "두"
    elif n == 3:
        return "세"
    elif n == 4:
        return "네"
    elif n == 5:
        return "다섯"
    elif n == 6:
        return "여섯"
    elif n == 7:
        return "일곱"
    elif n == 8:
        return "여덟"
    elif n == 9:
        return "아홉"
    elif n == 10:
        return "열"
    else:
        return -1
hour = koTime(clock.hour)
mi
watch = print("")