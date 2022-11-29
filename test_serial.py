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
A_PA = struct.pack("f", 1.0)
V_PA = struct.pack("f", 1.0)
A_PW = struct.pack("B", 1)
V_PW = struct.pack("B", 1)
A_Sense = struct.pack("f", 1)
V_Sense = struct.pack("f", 1)
A_R = struct.pack("H", 1)
V_R = struct.pack("H", 1)
PVARP = struct.pack("H", 1)
Act_thres = struct.pack("B", 1)
React_time = struct.pack("B", 1)
Response_factor = struct.pack("B", 1)
Recovery_time = struct.pack("H", 1)



Signal_set = Start + Fn_set + Pacing_mode + LRL + URL + MSR + A_PA + V_PA + A_PW + V_PW + A_Sense + V_Sense + A_R + V_R + PVARP + Act_thres + React_time + Response_factor + Recovery_time
Signal_echo = Start + SYNC + Pacing_mode + LRL + URL + MSR + A_PA + V_PA + A_PW + V_PW + A_Sense + V_Sense + A_R + V_R + PVARP + Act_thres + React_time + Response_factor + Recovery_time

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_set)

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_echo)
    data = pacemaker.read(49)
    Pacing_mode = data[0]
    LRL = data[1]
    URL = data[2]
    MSR = data[3]
    A_PA = struct.unpack("f", data[4:8])[0]
    V_PA = struct.unpack("f", data[8:12])[0]
    A_PW = data[12]
    V_PW = data[13]
    A_Sens = struct.unpack("f", data[14:18])[0]
    V_Sens = struct.unpack("f", data[18:22])[0]
    A_R = struct.unpack("H", data[22:24])[0]
    V_R = struct.unpack("H", data[24:26])[0]
    PVARP = struct.unpack("H", data[26:28])[0]
    Act_thres = data[28]
    React_time = data[29]
    Response_factor = data[30]
    Recovery_time = struct.unpack("H", data[31:33])[0]
    Atr = struct.unpack("d", data[33:41])[0]
    Vnt = struct.unpack("d", data[41:49])[0]

print("From the board:")
print("Pacing_mode = ", Pacing_mode)
print("LRL = ", LRL)
print("URL = ", URL)
print("MSR = ",  MSR)
print("A_PA = ",  A_PA)
print("V_PA = ",  V_PA)
print("A_PW = ",  A_PW)
print("V_PW = ",  V_PW)
print("A_Sens = ",  A_Sens)
print("V_Sens = ",  V_Sens)
print("A_R = ",  A_R)
print("V_R = ",  V_R)
print("PVARP = ",  PVARP)
print("Act_thres = ",  Act_thres)
print("React_time = ",  React_time)
print("Response_factor = ",  Response_factor)
print("Recovery_time = ",  Recovery_time)
print("Atrial graph value = ", Atr)
print("Ventrical graph value = ", Vnt)
