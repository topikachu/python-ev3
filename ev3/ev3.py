import time
import threading
from rawdevice import analogdevice, dcm, iicdevice, lcd, motordevice, sound, uartdevice, ui, lms2012

UP_BUTTON = 0
ENTER_BUTTON = 1
DOWN_BUTTON = 2
RIGHT_BUTTON = 3
LEFT_BUTTON = 4
BACK_BUTTON = 5

_AMP_CIN = 22.0
_AMP_VIN = 0.5
_VCE = 0.05
_SHUNT_IN = 0.11
_AMP_COUT = 19.0
_SHUNT_OUT = 0.055

pollingThread = None
events = {}

SENSOR_1 = 0
SENSOR_2 = 1
SENSOR_3 = 2
SENSOR_4 = 3

MOTOR_A = 0
MOTOR_B = 1
MOTOR_C = 2
MOTOR_D = 3

MOTOR_A_BIT = 1
MOTOR_B_BIT = 2
MOTOR_C_BIT = 4
MOTOR_D_BIT = 8


def open_all_devices():
    analogdevice.open_device()
    dcm.open_device()
    iicdevice.open_device()
    lcd.open_device()
    motordevice.open_device()
    sound.open_device()
    uartdevice.open_device()
    ui.open_device()

    for port in range(0, 4):
        analogdevice.clear_change(port)
        uartdevice.reset(port)
        iicdevice.reset(port)


def close_all_devices():
    ui.close_device()
    uartdevice.close_device()
    sound.close_device()
    motordevice.close_device()
    lcd.close_device()
    iicdevice.close_device()
    dcm.close_device()
    analogdevice.close_device()


def get_battery():
    CinV = lms2012.CtoV(
        float(analogdevice.get_analog().BatteryCurrent)) / _AMP_CIN
    battery_v = lms2012.CtoV(
        float(analogdevice.get_analog().Cell123456)) / _AMP_VIN + CinV + _VCE
    battery_i = CinV / _SHUNT_IN
    motor_i = lms2012.CtoV(
        float(analogdevice.get_analog().MotorCurrent) / _AMP_COUT) / _SHUNT_OUT
    return battery_v, battery_i, motor_i


def registerEvent(predicate, handle):
    events[predicate] = handle


def is_up_button_pressed():
    return ui.is_pressed(UP_BUTTON)


def is_down_button_pressed():
    return ui.is_pressed(DOWN_BUTTON)


def is_left_button_pressed():
    return ui.is_pressed(LEFT_BUTTON)


def is_right_button_pressed():
    return ui.is_pressed(RIGHT_BUTTON)


def is_enter_button_pressed():
    return ui.is_pressed(ENTER_BUTTON)


def is_button_pressed(button):
    return ui.is_pressed(button)


LED_BLACK = 0
LED_GREEN = 1
LED_RED = 2
LED_ORANGE = 3
LED_GREEN_FLASH = 4
LED_RED_FLASH = 5
LED_ORANGE_FLASH = 6
LED_GREEN_PULSE = 7
LED_RED_PULSE = 8
LED_ORANGE_PULSE = 9


def set_led(light):
    return ui.set_led(light)


def run():
    while True:
        if ui.is_pressed(BACK_BUTTON):
            break
        for predicate, handle in events.iteritems():
            if predicate():
                handle()
        time.sleep(0)
