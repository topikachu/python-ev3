#!/usr/bin/env python
"""
Simple remote control. 

The motors are controlled according to the following table.

Motor port   Channel   Buttons
----------   -------   -------
    A           1        red
    B           1        blue
    C           2        red
    D           2        blue

The program is stopped by pressing the baecon button.
"""


from ev3.ev3dev import Motor, NoSuchMotorError
from ev3.lego import InfraredSensor
from ev3.event_loop import EventLoop

ir = InfraredSensor()


motors = []
for port in 'ABCD':
    try:
        motor = Motor(port=port)
        motor.regulation_mode = False
    except NoSuchMotorError:
        motor = None
    motors.append(motor)
    
buttons = [
    (ir.REMOTE.RED_UP, ir.REMOTE.RED_DOWN),
    (ir.REMOTE.BLUE_UP, ir.REMOTE.BLUE_DOWN),
]

def ir_changed(event):
    for channel in range(2):
        state = event.evaluation[channel]
        if state == ir.REMOTE.BAECON_MODE_ON:
            for m in motors:
                if m is not None:
                    m.stop()
            loop.stop()
        for button in range(2):
            n = channel * 2 + button
            motor = motors[channel * 2 + button]
            if not motor:
                pass
            elif state == buttons[button][0]:
                motor.run_forever(50)
            elif state == buttons[button][1]:
                motor.run_forever(-50)
            else:
                motor.stop()
    

loop = EventLoop()
loop.register_value_change(getter=lambda: ir.remote, 
                           startvalue=ir.remote,
                           target=ir_changed)
loop.start()
