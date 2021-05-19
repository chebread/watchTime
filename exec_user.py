# 디지털 시계
from datetime import *
import time
print("-- Time --")
n = 0
while True:
    # 값이 계속 바뀐다
    clock = datetime.now() # Flame
    watch = "%s년 %s월 %s일 %s시 %s분 %s초"%(clock.year, clock.month, clock.day, clock.hour, clock.minute, clock.second)
    print(watch)
    time.sleep(1) # 1 second
    n += 1
    if n == 3: # 값 변경시 출력값을 바꿉니다.
        break

