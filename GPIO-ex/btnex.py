import RPi.GPIO as GPIO
import time

# callable class
class BtnEx:
    def __init__(self):
        self.button_pin=16
        self.led_pin= 18
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led_pin, GPIO.OUT)

    def __call__(self):
        while 1:
            GPIO.output(self.led_pin,GPIO.input(self.button_pin))
            time.sleep(0.1)