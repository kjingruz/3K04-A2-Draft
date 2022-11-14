import serial

ser = serial.Serial('/dev/tty.usbmodem0000001234561')
print(ser.name)
ser.write(b'hello')
ser.close()
print("test file")