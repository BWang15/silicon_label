import serial
from constant import PORT, BR, acc_begin_idx, acc_end_idx, angular_velocity_begin_idx, angular_velocity_end_idx, \
    euler_angle_begin_idx, euler_angle_end_idx, acc_dic, angular_velocity_dic, euler_angle_dic


def HexStrAddSpace(HexStr):
    out_data = ''
    for i, s in enumerate(HexStr):
        if (i % 2 == 0) and i != 0:
            out_data += ' '
            out_data += s
        else:
            out_data += s
    return out_data.upper()


def deparse(MSB, LSB):
    aa = int(MSB, 16) << 8 | int(LSB, 16)
    if aa & 0x8000 == 0x8000:
        b = bin(aa)
        c = b[2:18]
        vv = []
        for i in c:
            if i == '1':
                vv.append(0)
            else:
                vv.append(1)
        s = ''
        for i in vv:
            s = s + str(i)
        aa = int(s, 2)
        c = ~aa
        return c
    else:
        return aa


def process_acc_data(components):
    for key, i in zip(acc_dic.keys(), range(7, 13)):
        acc_dic[key] = components[i]
    acc_x = deparse(acc_dic['x_MSB'], acc_dic['x_LSB']) / 8192
    acc_y = deparse(acc_dic['y_MSB'], acc_dic['y_LSB']) / 8192
    acc_z = deparse(acc_dic['z_MSB'], acc_dic['z_LSB']) / 8192
    return [acc_x, acc_y, acc_z]


def process_angular_velocity_data(components):
    for key, i in zip(angular_velocity_dic.keys(), range(13, 19)):
        angular_velocity_dic[key] = components[i]
    angular_velocity_x = deparse(angular_velocity_dic['x_MSB'], acc_dic['x_LSB']) / 8192
    angular_velocity_y = deparse(angular_velocity_dic['y_MSB'], acc_dic['y_LSB']) / 8192
    angular_velocity_z = deparse(angular_velocity_dic['z_MSB'], acc_dic['z_LSB']) / 8192
    return [angular_velocity_x, angular_velocity_y, angular_velocity_z]


def process_euler_angle_data(components):
    for key, i in zip(euler_angle_dic.keys(), range(19, 24)):
        euler_angle_dic[key] = components[i]
    euler_angle_x = deparse(euler_angle_dic['x_MSB'], acc_dic['x_LSB']) / 100
    euler_angle_y = deparse(euler_angle_dic['y_MSB'], acc_dic['y_LSB']) / 100
    euler_angle_z = deparse(euler_angle_dic['z_MSB'], acc_dic['z_LSB']) / 100
    return [euler_angle_x, euler_angle_y, euler_angle_z]

if __name__ == '__main__':
    ser = serial.Serial()
    ser.port = PORT
    ser.baudrate = BR
    ser.open()
    while 1:
        length = ser.in_waiting
        if length == 37:
            s = ser.read(length).hex()
            if s[6:10] == 'bfda':
                components = HexStrAddSpace(s).split(' ')
                acc_x, acc_y, acc_z = process_acc_data(components)
                angular_velocity_x, angular_velocity_y, angular_velocity_z = process_angular_velocity_data(components)
                euler_angle_x, euler_angle_y, euler_angle_z = process_euler_angle_data(components)
                print(acc_x, acc_y, acc_z)

        else:
            length = length + ser.in_waiting
            if length == 37:
                s = ser.read(length).hex()
                if s[6:10] == 'bfda':
                    components = HexStrAddSpace(s).split(' ')
                    acc_x, acc_y, acc_z = process_acc_data(components)
                    angular_velocity_x, angular_velocity_y, angular_velocity_z = process_angular_velocity_data(components)
                    euler_angle_x, euler_angle_y, euler_angle_z = process_euler_angle_data(components)
                    print(acc_x, acc_y, acc_z)
            else:
                pass
