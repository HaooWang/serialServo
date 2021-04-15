'''
FashionStar Uart舵机 
> 读取舵机的状态信息 <
--------------------------------------------------
- 作者: 阿凯
- Email: kyle.xing@fashionstar.com.hk
- 更新时间: 2020-12-5
--------------------------------------------------
'''
# 添加uservo.py的系统路径
import sys
sys.path.append("../../src")
# 导入依赖
import time
import serial
from uservo import UartServoManager

# 参数配置
# 角度定义
SERVO_PORT_NAME =  'COM7' # 舵机串口号
SERVO_BAUDRATE = 115200 # 舵机的波特率
SERVO_ID = 0  # 舵机的ID号

# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 初始化舵机管理器
uservo = UartServoManager(uart)

def log_servo_status():
    '''打印舵机状态'''
    # 读取温度
    voltage = uservo.query_voltage(SERVO_ID)
    # 读取电流
    current = uservo.query_current(SERVO_ID)
    # 读取功率
    power = uservo.query_power(SERVO_ID)
    # 读取温度
    temp = uservo.query_temperature(SERVO_ID)

    print("Voltage: {:4.1f}V; Current: {:4.1f}A; Power: {:4.1f}W; T: {:2.0f}℃".format(\
        voltage, current, power, temp), end='\r')

while True:
    uservo.set_servo_angle(SERVO_ID, 90)
    while not uservo.is_stop():
        log_servo_status()
        time.sleep(0.1)
    
    time.sleep(1)

    uservo.set_servo_angle(SERVO_ID, -90)
    while not uservo.is_stop():
        log_servo_status()
        time.sleep(0.1)

    time.sleep(1)