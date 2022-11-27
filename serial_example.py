import serial
import serial.tools.list_ports
import struct

# Mac ports, for windows you have to find the ports yourself
frdm_port = "/dev/cu.usbmodem0000001234561"

# B = uint8
# f = single
# H = uint16

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


Signal_set = Start + Fn_set + Pacing_mode + LRL + URL + MSR + A_V_PA + A_V_PW + A_V_Sense + A_V_R + PVARP + Act_thres + React_time + Response_factor + Recovery_time
Signal_echo = Start + SYNC + Pacing_mode + LRL + URL + MSR + A_V_PA + A_V_PW + A_V_Sense + A_V_R + PVARP + Act_thres + React_time + Response_factor + Recovery_time

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_set)

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_echo)
    data = pacemaker.read(13)
    Pacing_mode = data[0]
    LRL = data[1]
    URL = data[2]
    MSR = data[3]
    A_V_PA = data[4]
    A_V_PW = data[5]
    A_V_Sens = data[6]
    A_V_R = data[7]
    PVARP = data[8]
    Act_thres = data[9]
    React_time = data[10]
    Response_factor = data[11]
    Recovery_time = data[12]

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
