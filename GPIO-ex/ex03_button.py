#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def button_callback(channel):
    

# 사용할 GPIO 핀의 번호를 선정합니다.
button_pin = 15

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정 , PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_callback,bouncetime=10)

try:
    while 1:
        time.sleep(0,.1)
except
    # 만약 버튼핀에 High(1) 신호가 들어오면, "Button pushed!" 을 출력합니다.
if GPIO.input(button_pin) == GPIO.HIGH:
print("Button pushed!")
time.sleep(0.1) # 0.1초 딜레이