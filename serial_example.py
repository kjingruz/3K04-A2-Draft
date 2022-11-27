import serial
import serial.tools.list_ports
import struct

# Mac ports, for windows you have to find the ports yourself
frdm_port = "/dev/cu.usbmodem0000001234561"

# B = uint8
# f = single
# H = uint16
# d = double ( 8 bytes)

Start = b'\x16'
SYNC = b'\x22'
Fn_set = b'\x55'
Pacing_mode = struct.pack("B", 1)
LRL = struct.pack("B", 1)
URL = struct.pack("B", 1)
MSR = struct.pack("B", 1)
A_V_PA = struct.pack("f", 1.0)
A_V_PW = struct.pack("B", 1)
A_V_Sense = struct.pack("B", 1)
A_V_R = struct.pack("H", 1)
PVARP = struct.pack("H", 1)
Act_thres = struct.pack("B", 1)
React_time = struct.pack("B", 1)
Response_factor = struct.pack("B", 1)
Recovery_time = struct.pack("B", 1)



Signal_set = Start + Fn_set + Pacing_mode + LRL + URL + MSR + A_V_PA + A_V_PW + A_V_Sense + A_V_R + PVARP + Act_thres + React_time + Response_factor + Recovery_time + Atr + Vnt
Signal_echo = Start + SYNC + Pacing_mode + LRL + URL + MSR + A_V_PA + A_V_PW + A_V_Sense + A_V_R + PVARP + Act_thres + React_time + Response_factor + Recovery_time

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_set)

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_echo)
    data = pacemaker.read(18)
    Pacing_mode = data[0]
    LRL = data[1]
    URL = data[2]
    MSR = data[3]
    A_V_PA = struct.unpack("f", data[4:8])[0]
    A_V_PW = data[8]
    A_V_Sens = data[9]
    A_V_R = struct.unpack("H", data[10:12])[0]
    PVARP = struct.unpack("H", data[12:14])[0]
    Act_thres = data[14]
    React_time = data[15]
    Response_factor = data[16]
    Recovery_time = data[17]
    Atr = struct.unpack("d", data[18:26])[0]
    Vnt = struct.unpack("d", data[26:34])[0]

print("From the board:")
print("Pacing_mode = ", Pacing_mode)
print("LRL = ", LRL)
print("URL = ", URL)
print("MSR = ",  MSR)
print("A_V_PA = ",  A_V_PA)
print("A_V_PW = ",  A_V_PW)
print("A_V_Sens = ",  A_V_Sens)
print("A_V_R = ",  A_V_R)
print("PVARP = ",  PVARP)
print("Act_thres = ",  Act_thres)
print("React_time = ",  React_time)
print("Response_factor = ",  Response_factor)
print("Recovery_time = ",  Recovery_time)
print("Atrial graph value = ", Atr)
print("Ventrical graph value = ", Vnt)
