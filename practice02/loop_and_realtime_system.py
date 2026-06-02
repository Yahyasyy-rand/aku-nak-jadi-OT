import time
import random

mesin = False

while True:
    perintah = input("start / stop :")
    suhu = random.randint(60, 100)

    if perintah == "start" and suhu < 80:
        mesin = True
    else:
        mesin = False

    print(f"Suhu: {suhu} | Mesin: {"on" if mesin else "off"}")

    time.sleep(1)