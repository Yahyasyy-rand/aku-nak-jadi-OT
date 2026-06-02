mesin = False

while True :
    perintah = input("masukkan perintah: ")

    if perintah == "start":
        mesin = True
    elif perintah == "stop":
        mesin = False
    
    print("status mesin:", "on" if mesin else "off")