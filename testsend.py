import serial

ser = serial.Serial('/dev/tty.usbmodem0000001234561',9600)
print(ser.name)
ser.write(1.0)
ser.close()
print("test file")