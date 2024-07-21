# -*- coding: utf-8 -*-
"""
MQ2

@author: User
"""
import machine
import time

mq2_pin = machine.ADC(26)

def read_mq2():
    gas_level = mq2_pin.read_u16()
    return gas_level

while True:
    gas_level = read_mq2()
    print("Gas Level:", gas_level)
    time.sleep(2)

