import serial

ser = serial.Serial('COM5',9600)    #check COM
print(ser.name)
text = ser.readline()
print(text)