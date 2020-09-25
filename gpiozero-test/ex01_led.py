from gpiozero import LED
from time import sleep

red = LED(18)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)

# red.blink()
# pause()
# 위 코드로 blink 할 수 있음