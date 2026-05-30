import time
import random

data_suhu = []
counter_bahaya = 0

while True:
    suhu = random.randint(60, 100)

    data_suhu.append(suhu)

    if len(data_suhu) > 5:
        data_suhu.pop(0)

    rata = sum(data_suhu) /len(data_suhu)

    if suhu > 85:
        counter_bahaya += 1
        status = "Bahaya"

    else:
        counter_bahaya = 0
        status = "Normal"

    if counter_bahaya >= 3:
        alarm = "Alarm aktif"

    else:
        alarm = "-"

    waktu = time.strftime("%H:%M:%S")

    print(f"Waktu: {waktu} | Suhu: {suhu} | Rata=rata: {rata:.2f} | Status: {status} | {alarm}")

    time.sleep(2)