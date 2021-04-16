#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Copyright:  Jihua Lab 2021.
@File    :   ping_debug.py    
@Author :   HaoWANG, Foshan，China
@Contact :   wanghao@jihualab.com
@License :   JHL ( not BSD)

@Description:  


@Create Time   :   2021/4/16  10:56
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/16 10:56   wanghao      1.1.0         None
'''

# import lib

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
SERVO_PORT_NAME = 'COM3'  # 舵机串口号
SERVO_BAUDRATE = 115200  # 舵机的波特率
SERVO_ID = 0  # 舵机的ID号

# 初始化并自动获取舵机串口号
uservo_init = UsInit(logger_level="INFO",scan_servo_port=False)
uservo_init.set_logging_mode()
# SERVO_PORT_NAME = uservo_init.get_servo_port_name()

# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE, \
                     parity=serial.PARITY_NONE, stopbits=1, \
                     bytesize=8, timeout=0)
# 初始化舵机管理器
uservo = UartServoManager(uart, is_scan_servo=False,is_debug=True)

# 舵机扫描
print("开始进行舵机扫描")
uservo.scan_servo()
servo_list = list(uservo.servos.keys())
print("舵机扫描结束, 舵机列表: {}".format(servo_list))

# 舵机通讯检测
is_online = uservo.ping(SERVO_ID,with_logging_info=True)
print("舵机ID={} 是否在线: {}".format(SERVO_ID, is_online))


