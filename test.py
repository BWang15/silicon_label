import serial
import binascii


acc_begin_idx = 14
acc_end_idx = 26
angular_velocity_begin_idx = 26
angular_velocity_end_idx = 38
euler_angle_begin_idx = 38
euler_angle_end_idx = 50
"""
acc_begin_idx = 7
acc_end_idx = 13
angular_velocity_begin_idx = 13
angular_velocity_end_idx = 19
euler_angle_begin_idx = 19
euler_angle_end_idx = 25
"""
# Yaw,Pitch,Roll

def bytes2hex(byte_arr: bytes) -> str:
    return byte_arr.hex()
def deparse(hex_array: str) -> dict:
    d = {
        'x' : 0,
        'y' : 0,
        'z' : 0
        }
    d['x'] = int(hex_array[: 4], 16)
    d['y'] = int(hex_array[4: 8], 16)
    d['z'] = int(hex_array[8:], 16)
    #d['x'] = int.from_bytes(binascii.a2b_hex(hex_array[: 4]), "big")
    #d['y'] = int.from_bytes(binascii.a2b_hex(hex_array[4: 8]), "big")
    #d['z'] = int.from_bytes(binascii.a2b_hex(hex_array[8:]), "big")
    return d
def process_euler_angle(dic: dict) -> dict:
    d = {
        'x' : 0,
        'y' : 0,
        'z' : 0
        }
    for key in dic.keys():
        d[key] = dic.get(key)/100
        
    return d

def process_acceleration(dic: dict, scale: int) -> dict:
    d = {
        'x' : 0,
        'y' : 0,
        'z' : 0
        }
    for key in dic.keys():
        d[key] = dic.get(key)/32768 * scale
        
    return d


ser = serial.Serial("/dev/ttyUSB0", 115200)
#ser.open()
while (1):
    s = ser.read(200)
    print(s)
    print('')
    res_hex = bytes2hex(s)
    #print(res_hex[6:11])
    #print(s[5:7])
    if res_hex[6:10] == 'bfda':
        acc = s[7:14]
        x = int.from_bytes(acc[:3], 'big')
        y = int.from_bytes(acc[3:5], 'big')
        z = int.from_bytes(acc[5:], 'big')
        #print(x, y, z)
        x = x/32768 * 4
        y = y/32768 * 4
        z = z/32768 * 4
        #print(x, y, z)
        #acc_d = process_acceleration(deparse(acc), 4)
        #print(acc_d)
        '''
        temp = res_hex[50:54]
        print(int(temp, 16) / 132.48 + 25)
        acc = res_hex[acc_begin_idx:acc_end_idx]
        angular_velocity = res_hex[angular_velocity_begin_idx:angular_velocity_end_idx]
        euler_angle = res_hex[euler_angle_begin_idx:euler_angle_end_idx]
        acc_d = deparse(acc)
        angular_velocity_d = deparse(angular_velocity)
        euler_angle_d = deparse(euler_angle)
        '''
        #print(process_acceleration(acc_d, 4), angular_velocity_d, euler_angle_d)