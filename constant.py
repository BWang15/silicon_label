'''
http://www.gzlwkj.com/static-file/LinkPG-Kit-Datasheet(CodeV5.3).pdf
https://blog.csdn.net/zcs_xueli/article/details/108046010
https://blog.csdn.net/weixin_31328141/article/details/114567343
'''

BR = 115200
PORT = 'COM3'

"""
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

acc_dic = {
    'x_MSB': '00',
    'x_LSB': '00',
    'y_MSB': '00',
    'y_LSB': '00',
    'z_MSB': '00',
    'z_LSB': '00'
}
angular_velocity_dic = {
    'x_MSB': '00',
    'x_LSB': '00',
    'y_MSB': '00',
    'y_LSB': '00',
    'z_MSB': '00',
    'z_LSB': '00'
}
euler_angle_dic = {
    'x_MSB': '00',
    'x_LSB': '00',
    'y_MSB': '00',
    'y_LSB': '00',
    'z_MSB': '00',
    'z_LSB': '00'
}