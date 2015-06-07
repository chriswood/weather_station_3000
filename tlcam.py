#!/usr/bin/python

import pygame
from pygame import camera
import time

img_dir = '/home/pi/imgs'
interval = 5*60 #seconds
limit = 100

camera.init()
camera.list_cameras()
cam = camera.Camera("/dev/video0", (640, 480))

pic_count = 0
while pic_count < limit:
    image_name = "{0}/outside_{1}.jpg".format(img_dir, pic_count)
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, image_name)
    cam.stop()
    pic_count += 1
    time.sleep(interval)
