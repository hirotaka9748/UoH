import serial
import time
from struct import *

def tesla(path1):
    path = path1
    ser = serial.Serial("COM6", 19200, timeout = 0.5)
    recv_data = ser.read(5)
    ser.close()

    str_data = recv_data.hex()
    cut_data = str_data[str_data.find("a2")+2:]
    cut2_data = cut_data[0:4]

    bytes_data = bytes.fromhex(cut2_data)
    int_data = int.from_bytes(bytes_data, 'big', signed=True)
    result = int_data / 10
    print(result)
    with open(path1, 'a') as f:
        print(result,file=f)
    time.sleep(0.3)
        
    