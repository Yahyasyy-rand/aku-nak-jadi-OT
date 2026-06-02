import random

mesin = False

perintah = input("start / stop :")
suhu = random.randint(60, 100)

if perintah == "start" and suhu < 80:
    mesin = True
else:
    mesin = False

print("suhu:", suhu)
print("status mesin:", "on" if mesin else "off")