import time
import requests as requests
import serial
try:
    ad = serial.Serial("COM3",9600)
    def ledon():
        str = '1'
        ad.write(str.encode())
    def ledoff():
        str = '0'
        ad.write(str.encode())

    r = requests.get('https://pythonreq-a49d5-default-rtdb.firebaseio.com/.json')
    status = r.json()
    key = status['status']
    print(f"Your last command is, {key}!")


    while True:
        r = requests.get('https://pythonreq-a49d5-default-rtdb.firebaseio.com/.json')
        status = r.json()
        key = status['status']
        v = key
        v = v.strip()
        if v == "1":
            ledon()
        if v == "0":
            ledoff()
        if v == "stop":
            break
        time.sleep(1)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("Your device hasn't internet!. Please,try again!")
