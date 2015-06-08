import os
import gps
from gps import gps, WATCH_ENABLE 
from time import sleep
from threading import Thread
 

class GpsPoller(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.current_value = None
        self.running = True #setting the thread running to true
 
    def run(self):
        while self.running:
            self.gpsd.next()

    def display(self):
        try:
            self.start()
            while True:
                os.system('clear')
                print
                print('Latitude:{:>30}'.format(self.gpsd.fix.latitude))
                print('Longitude:{:>30}'.format(self.gpsd.fix.longitude))
                sleep(5)
        except(KeyboardInterrupt, SystemExit):
            print('exiting...')
            self.running = False
            self.join()
            print('shut down')

if __name__ == '__main__':
    gp = GpsPoller() # create the thread
    gp.display()
        #print ' GPS reading'
        #print '----------------------------------------'
        #print 'latitude    ' , gpsd.fix.latitude
        #print 'longitude   ' , gpsd.fix.longitude
        #print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
        #print 'altitude (m)' , gpsd.fix.altitude
        #print 'eps         ' , gpsd.fix.eps
        #print 'epx         ' , gpsd.fix.epx
        #print 'epv         ' , gpsd.fix.epv
        #print 'ept         ' , gpsd.fix.ept
        #print 'speed (m/s) ' , gpsd.fix.speed
        #print 'climb       ' , gpsd.fix.climb
        #print 'track       ' , gpsd.fix.track
        #print 'mode        ' , gpsd.fix.mode
        #print
        #print 'sats        ' , gpsd.satellites
