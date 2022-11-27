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
    data = pacemaker.read(4)
    red_rev = data[0]
    green_rev = data[1]
    blue_rev = data[2]
    off_rev = data[3]
    #switch_rev =  struct.unpack("H", data[7:9])[0]

print("From the board:")
print("red_en = ", red_rev)
print("green_en = ", green_rev)
print("blue_en = ", blue_rev)
print("off_time = ",  off_rev)
#print("switch_time = ", switch_rev)