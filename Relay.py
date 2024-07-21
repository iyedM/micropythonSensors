# -*- coding: utf-8 -*-
"""
Relay  Module
@author: User
"""

import machine
import time

relay_pin = machine.Pin(18, machine.Pin.OUT)

def control_relay(state):
    relay_pin.value(state)

while True:
    control_relay(1)  # Turn on the relay
    print("lamp")
    time.sleep(5)
    control_relay(0)  # Turn off the relay
    print("lamp off")
    time.sleep(5)
