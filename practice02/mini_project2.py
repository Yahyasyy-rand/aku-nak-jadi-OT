import time
import random

mesin = False

while True:
    perintah = input("start / stop: ")
    suhu = random.randint(60, 100)

    if perintah == "start" and suhu < 80:
        mesin = True

    if suhu >= 85:
        mesin = False
        print("!!! SAFETY SHUTDOWN !!!")

    if perintah == "stop":
        mesin = False

    print(f"Suhu: {suhu} | Mesin: {'ON' if mesin else 'OFF'}")
    print("------------------------")

    time.sleep(1)