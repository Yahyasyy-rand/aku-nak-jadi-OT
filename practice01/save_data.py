import time
import random

file = open("data_suhu.txt", "a")

for i in  range(10):
    suhu = random.randint(60, 100)

    data = f"suhu: {suhu}\n"
    file.write(data)

    if suhu > 85:
        status = "Bahaya, Suhu terlalu tinggi"
    elif suhu < 65:
        status = "Bahaya, Suhu terlalu rendah"
    else:
        status = "Suhu normal"

    print(f"Suhu: {suhu} | Status: {status}")
    time.sleep(1)

file.close()