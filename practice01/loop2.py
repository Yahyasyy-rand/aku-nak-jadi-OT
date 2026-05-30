import time
import random

while True:
    suhu = random.randint(60, 100)
    print("Suhu:", suhu)

    if suhu > 85:
        print("Bahaya, Suhu terlalu tinggi")
    elif suhu < 65:
        print("Bahaya, Suhu terlalu rendah")
    else:
        print("Suhu normal")
    
    print("memantau suhu...")
    time.sleep(2)
    