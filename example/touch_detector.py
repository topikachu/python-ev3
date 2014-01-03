from ev3 import ev3
from ev3.sensor.lego import EV3TouchSensor

ev3.open_all_devices()
touch_sensor = EV3TouchSensor(ev3.SENSOR_1)
ev3.registerEvent(lambda: touch_sensor.is_pressed() is True, lambda: print('hello'))
ev3.start()
ev3.close_all_devices()
