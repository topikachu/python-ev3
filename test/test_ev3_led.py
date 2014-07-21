from ev3.ev3dev import  LED
import unittest
import time
from util import get_input

class TestLED(unittest.TestCase):

    def test_led(self):
        get_input('Test LED')
        led = LED()
        get_input('Test left red')
        led.left.color=LED.COLOR.RED
        get_input('Test left green')
        led.left.color=LED.COLOR.GREEN
        get_input('Test left amber')
        led.left.color=LED.COLOR.AMBER
        get_input('Test right blink')
        led.right.blink(color=LED.COLOR.GREEN,delay_on=1000, delay_off=2000 )
        time.sleep(10)
        get_input('Test left and right on')
        led.left.on()
        led.right.on()
        time.sleep(5)
        get_input('Test left and right off')
        led.left.off()
        led.right.off()
        
        
if __name__ == '__main__':
    unittest.main()
