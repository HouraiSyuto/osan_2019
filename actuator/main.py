from m5stack import *
from machine import Pin
import utime

utime.sleep(2)
lcd.clear()
lcd.setCursor(0, 0)
lcd.setColor(lcd.WHITE)
lcd.print("Hi!\n")

# モーターをつなぐピン
motor1 = Pin(1, Pin.OUT)
motor2 = Pin(3, Pin.OUT)
lcd.print("PINs initialized!\n")

actuator_status = { 
    'started': False, 'reversed': False, 'stopped': False 
}

def set_started():
    actuator_status['started']  = True
    actuator_status['reversed'] = False
    actuator_status['stopped']  = False

def set_reversed():
    actuator_status['started']  = False
    actuator_status['reversed'] = True
    actuator_status['stopped']  = False

def set_stopped():
    actuator_status['started']  = False
    actuator_status['reversed'] = False
    actuator_status['stopped']  = True

def is_started():
    return actuator_status['started'] 

def is_reversed():
    return actuator_status['reversed']

def is_stopped():
    return not is_started() and not is_reversed()

def start():
    motor1.value(1)
    motor2.value(0)
    set_started()
     
def reverse():
    motor1.value(0)
    motor2.value(1)
    set_reversed()

def stop():
    toggle()
    utime.sleep(0.5)

    motor1.value(0)
    motor2.value(0)
    set_stopped()

def toggle():
    if not is_stopped():
        if is_started():
            reverse()
        else:
            start()

while True:
    if buttonA.wasPressed() and not is_started():
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.print("button A pressed.\n")
        
        start()
        
    if buttonB.isPressed() and not is_reversed():
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.print("button B pressed.\n")

        reverse()
     
    if buttonC.isPressed() and not is_stopped():
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.print("button C pressed.\n")

        stop()
