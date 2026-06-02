import random
import time

mesin = False

suhu = random.randint(60, 100)

if suhu < 80:
    mesin = True
else:
    mesin = False


print("suhu:", suhu)
print("status mesin:", "on" if mesin else "off")
