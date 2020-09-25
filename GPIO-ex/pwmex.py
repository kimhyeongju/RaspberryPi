import RPi.GPIO as GPIO
import time

# callable class
class PwmEx:
    def __init__(self):
        self.led_pin= 18
        
        GPIO.setup(self.led_pin, GPIO.OUT)
        self.p = GPIO.PWM(self.led_pin, 50)
        self.p.start(0)

    def __call__(self):
        try:
            while 1:
                # fade in
                for dc in range(0,101,5):
                    self.p.ChangeDutyCycle(dc)
                    time.sleep(0.1)

                # fade out
                for dc in range(100,-1,-5):
                    self.p.ChangeDutyCycle(dc)
                    time.sleep(0.1)

        except KeyboardInterrupt:
            self.p.stop()