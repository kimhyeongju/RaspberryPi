from piapp import *
import RPi.GPIO as GPIO

from ledex import LedEx
from btnex import BtnEx
from btneventex import BtnEventEx
from pwmex import PwmEx
from pwmservoex import PwmServoEx
from ultraex import UltraEx
from mcpex import McpEx

class GpioApp(PiApplication):
    def __init__(self):
        super().__init__()
    
    def create_menu(self,menu):
        menu.add_menu(MenuItem("종료",self.exit))
        menu.add_menu(MenuItem("LED",LedEx())) # action = LedEx()와 같음
        menu.add_menu(MenuItem("Button",BtnEx()))
        menu.add_menu(MenuItem("Button Event",BtnEventEx()))
        menu.add_menu(MenuItem("PWM",PwmEx()))
        menu.add_menu(MenuItem("Servo",PwmServoEx()))
        menu.add_menu(MenuItem("Ultra",UltraEx()))
        menu.add_menu(MenuItem("조도",McpEx()))


if __name__ == "__main__":
    app = GpioApp()
    app.run()
