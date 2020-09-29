import time
from picamera import picamera
import numpy as np
import cv2

with picamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)

    output = np.empty((240,320,3), dtype=np.uint8)
    # camera.capture(output, 'rgb')
    camera.capture(output,'bgr')

    cv2.imshow('frame', output)
    cv2.waitkey(0)

    cv2.destryAllwindows()