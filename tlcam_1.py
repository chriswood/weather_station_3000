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

image_name = "{0}/outside_test.jpg".format(img_dir)
cam.start()
img = cam.get_image()
pygame.image.save(img, image_name)
cam.stop()
