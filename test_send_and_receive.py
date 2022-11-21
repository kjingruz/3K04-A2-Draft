import serial

#ser = serial.Serial('/dev/tty.usbmodem0000001234561',115200) #mac
ser = serial.Serial('COM4',115200) #windows
print(ser.name)

enter = [0x16, 0x55, 0x1, 0x32, 0x32, 0x32, 0x5, 0x1, 0x0, 0x96, 0x96, 0x1, 0xA, 0x1, 0x2] #hex
enter = [0x16, 0x22, 0x1, 0x32, 0x32, 0x32, 0x5, 0x1, 0x0, 0x96, 0x96, 0x1, 0xA, 0x1, 0x2] #hex

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
text = ser.read()   
print(text)
text = ser.read()   
print(text)
text = ser.read()   
print(text)

#first 8
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
text = ser.read()   
print(text)
text = ser.read()   
print(text)
text = ser.read()   
print(text)

#second 8
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
text = ser.read()   
print(text)
text = ser.read()   
print(text)
text = ser.read()   
print(text)



ser.close()
