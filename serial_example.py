import serial
import serial.tools.list_ports
import struct

# Mac ports, for windows you have to find the ports yourself
frdm_port = "/dev/cu.usbmodem0000001234561"

Start = b'\x16'
SYNC = b'\x22'
Fn_set = b'\x55'
red_en = struct.pack("B", 1)
green_en = struct.pack("B", 0)
blue_en = struct.pack("B", 1)
off_time = struct.pack("B", 1)

Signal_set = Start + Fn_set + red_en + green_en + blue_en + off_time
Signal_echo = Start + SYNC + red_en + green_en + blue_en + off_time

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