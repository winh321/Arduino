import serial
ad = serial.Serial("COM3",9600)
def ledon():
	str = '1'
	ad.write(str.encode())
def ledoff():
	str = '0'
	ad.write(str.encode())
while True:
	v = input("input 1 or 0 : ")
	v = v.strip()
	if v== "1":
		ledon()
	if v=="0":
		ledoff()
	if v =="stop":
		break
print("This program was end successfully.")

	
