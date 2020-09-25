from piapp import *
import RPi.GPIO as GPIO

class GpioApp(PiApplication):
    def __init__(self):
        super().__init__()
    
    def create_menu(self,menu):
        # 1. LED
        # 2. 버튼
        # 3. 버튼 이벤트
        menu.add_menu()
        menu.add_menu()
        menu.add_menu()
if __name__ == "__main__":
    app = GpioApp()
    app.run()
