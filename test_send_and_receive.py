import serial

#ser = serial.Serial('/dev/tty.usbmodem0000001234561',115200) #mac
ser = serial.Serial('COM4',115200) #windows
print(ser.name)
enter = [0x16, 0x22, 0x1, 0x1, 0x0, 0x3] #dec
ser.write(enter)
print("test file sent")

text = ser.read()
print(text)
text = ser.read()
print(text)
text = ser.read()
print(text)
text = ser.read()
print(text)
text = ser.read()
print(text)

ser.close()
