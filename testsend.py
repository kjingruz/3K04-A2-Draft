import serial

ser = serial.Serial('/dev/tty.usbmodem0000001234561',115200)
print(ser.name)
enter = [0x16, 0x55, 0x1, 0x1, 0x0, 0x3] #dec
# hexnum = []
# for i in enter:
#     hexnum.append(hex(i))
#ser.open()
ser.write(enter)
ser.close()
print("test file")