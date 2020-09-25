#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 선정합니다.
button_pin = 15
led_pin= 18

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정 , PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED핀의 OUT설정
GPIO.setup(led_pin, GPIO.OUT)

light_on = False

# button_callback 함수를 정의합니다.
def button_callback(channel):
    global light_on # Global 변수선언
    if light_on == False: # LED 불이 꺼져있을때
        GPIO.output(led_pin,1) # LED ON
        print("LED ON!")
    else: # LED 불이 져있을때
        GPIO.output(led_pin,0) # LED OFF
        print("LED OFF!")
    light_on = not light_on # False <=> True

# Event 알림 방식으로 GPIO 핀의 Rising 신호를 감지하면 button_callback 함수를 실행
# 300ms 바운스타임을 설정하여 잘못된 신호를 방지합니다.
GPIO.add_event_detect(button_pin,GPIO.RISING, callback=button_callback,
bouncetime=10)

try:
    while 1:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
