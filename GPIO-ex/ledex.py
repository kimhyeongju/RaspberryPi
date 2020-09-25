import RPi.GPIO as GPIO
import time

# callable class
class LedEx:
    def __init__(self):
        self.led_pin = 18
        GPIO.setup(self.led_pin, GPIO.OUT)

    def __call__(self):     # 클래스를 함수처럼 쓰기위해 반드시 필요한 메서드, 없으면 18 line은 에러
        for i in range(10):
            GPIO.output(self.led_pin,1)  # LED ON
            time.sleep(1)           # 1초동안 대기상태
            GPIO.output(self.led_pin,0)  # LED OFF
            time.sleep(1)

# if __name__ == "__main__":
#     ex = LedEx()    # LedEx 인스턴스, 생성자 호출
    
#     # C++에서,
#     # LedEx ex;     정적 할당(파이썬은 정적할당 없음)
#     # LedEx *ex = new LedEx();  동적 할당

#     ex()    # LedEx 클래스의 __call__() 메서드 호출
