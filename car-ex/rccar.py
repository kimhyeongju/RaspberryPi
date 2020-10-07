from btsocket import btsocket
from bluetooth import *

from gpiozero import Robot
from time import sleep

car = Robot(left=(17,27,22), right=(15,18,14), pwm=True)

def control(tokens):
    command = int(tokens[0])
    if command == 0:     # 주행 모드
        x = int(tokens[1])
        y = int(tokens[2])
    
    elif command == 1:  # 카메라 모드
        angle = int(tokens[1])
        servo.angle = angle

client_socket = btsocket( RFCOMM )
client_socket.connect(("00:18:91:D7:A1:D1", 1))

try:
    while True:
        line = client_socket.readline()
        control(line.split(','))
except KeyboardInterrupt:
    print("Finished")

client_socket.close()