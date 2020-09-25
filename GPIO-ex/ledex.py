import RPi.GPIO as GPIO
import time

# callable class
class LedEx:
    def __init__(self):
        pass
    def __call__(self):     # 클래스를 함수처럼 쓰기위해 반드시 필요한 메서드, 없으면 17 line은 에러
        print("LedEx call")

if __name__ == "__main__":
    ex = LedEx()    # LedEx 인스턴스, 생성자 호출
    
    # C++에서,
    # LedEx ex;     정적 할당(파이썬은 정적할당 없음)
    # LedEx *ex = new LedEx();  동적 할당

    ex()    # LedEx 클래스의 __call__() 메서드 호출
