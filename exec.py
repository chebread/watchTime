# 고전 시계
from datetime import *
print("-- 시계 --")
clock = datetime.now() # Flame
watch = "%s년 %s월 %s일 %s시 %s분 %s초"%(clock.year, clock.month, clock.day, clock.hour, clock.minute, clock.second)
print(watch)