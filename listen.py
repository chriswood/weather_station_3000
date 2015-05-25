import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)

# GPIO.setwarnings(False)

GPIO.setup(14, GPIO.IN)

while True:
    try:  
        GPIO.wait_for_edge(14, GPIO.FALLING)
        os.system("python /home/pi/library/weather_station_3000.py")
        time.sleep(5)  
    except KeyboardInterrupt:  
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit  



#while True:
#    if GPIO.input(14) == False:
#        print("pushed")
#        os.system("python /home/pi/library/weather_station_3000.py")
#        time.sleep(5)
