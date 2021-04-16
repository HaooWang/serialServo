'''
FashionStar Uart舵机 
> 舵机扫描 <
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
SERVO_PORT_NAME =  'COM3' # 舵机串口号
SERVO_BAUDRATE = 115200 # 舵机的波特率

# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 初始化舵机管理器
uservo = UartServoManager(uart,is_scan_servo=True)

# 舵机扫描
print("开始进行舵机扫描")
uservo.scan_servo()
servo_list = list(uservo.servos.keys())
print("舵机扫描结束, 舵机列表: {}".format(servo_list))