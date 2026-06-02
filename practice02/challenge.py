import random
import time

mesin = False

while True:
    perintah = input("start / stop: ")
    suhu = random.randint(60, 100)
    
    if suhu < 75:
        status = "normal"
    elif suhu <= 85:
        status = "warning"
    else:
        status = "danger"
    
    if perintah == "start" and suhu < 80:
        print("mesin menyala dalam 3 detik...")
        time.sleep(3)
        mesin = True

    if suhu > 80:
        print("!!! WARNING: SUHU MULAI TINGGI !!!")

    if suhu >= 85:
        print("!!! SAFETY SHUTDOWN !!!")
        mesin = False
    
    if perintah == "stop":
        mesin = False

    print(f"Suhu: {suhu} | Status: {status} | Mesin: {'ON' if mesin else 'OFF'}")
    print("------------------------")

    time.sleep(1)