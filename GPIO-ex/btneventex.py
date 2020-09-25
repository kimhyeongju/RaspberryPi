import RPi.GPIO as GPIO
import time

# callable class
class BtnEventEx:
    def __init__(self):
        # 사용할 GPIO핀 번호 설정
        self.button_pin=16
        self.led_pin= 18

        # 버튼핀의 INPUT, PULL DOWN 설정
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led_pin, GPIO.OUT)
        self.light_on = False
    
    def button_callback(self,channel):
        if self.light_on == False:  # LED불이 켜져있을때
            GPIO.output(self.led_pin,1) # LED ON
            print("LED ON")
        else:
            GPIO.output(self.led_pin,0) # LED불이 꺼졌을떄 LED OFF
            print("LED OFF")
        self.light_on = not self.light_on   # False <=> True

    def __call__(self): 
        self.light_on = False
        GPIO.add_event_detect(self.button_pin,GPIO.RISING, callback=self.button_callback,bouncetime=10)

        try:
            while 1:
                time.sleep(0.1)
        except KeyboardInterrupt:
            GPIO.remove_event_detect(self.button_pin)

