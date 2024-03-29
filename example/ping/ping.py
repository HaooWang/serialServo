
# 添加uservo.py的系统路径
import sys

sys.path.append("../../src")
# 导入依赖
import time
import serial
import logging

from uservo import UartServoManager, UsInit

# 参数配置
# 角度定义
SERVO_PORT_NAME = ''  # 舵机串口号
SERVO_BAUDRATE = 115200  # 舵机的波特率
SERVO_ID = 0  # 舵机的ID号

# 自动获取舵机串口号
sys_init = UsInit()

# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE, \
                     parity=serial.PARITY_NONE, stopbits=1, \
                     bytesize=8, timeout=0)
logging.info("舵机串口初始化{}".format(uart))
# 初始化舵机管理器
uservo = UartServoManager(uart, is_debug=True)

# 舵机通讯检测
is_online = uservo.ping(SERVO_ID)
print("舵机ID={} 是否在线: {}".format(SERVO_ID, is_online))
