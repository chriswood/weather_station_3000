#!/usr/bin/python
#
import sqlite3
import Adafruit_BMP.BMP085 as BMP
import Adafruit_DHT as DHT
import sys

ALTITUDE_EST = 12.0
SLP_EST = 102150.0
DB = '/home/pi/library/weather.db'

class Weather:
    def __init__(self):
        self.alt_est = ALTITUDE_EST
        self.slp_est = SLP_EST
        # Actually BMP185, but drivers are the same
        self.sensor_p = BMP.BMP085(mode=BMP.BMP085_ULTRAHIGHRES)
        self.sensor_h = DHT.DHT11
        self.dht_pin = 4
        
    def connect_db(self):
        try:
            self.conn = sqlite3.connect(DB)
            self.c = self.conn.cursor()
        except:
            print("Could not connect sqlite3 to db.")
            sys.exit(1)

    def get_humidity(self):
        return DHT.read_retry(self.sensor_h, self.dht_pin) 
    
    def c_to_f(self, temp_c):
        return (9.0/5.0)*temp_c + 32.0
 
    def save_data(self):
        self.connect_db()

        temp = self.sensor_p.read_temperature(scale='f')
        pressure = self.sensor_p.read_pressure()
        sl_pressure = self.sensor_p.read_sealevel_pressure(altitude_m=ALTITUDE_EST)
        altitude = self.sensor_p.read_altitude(sealevel_pa=SLP_EST)
        print("temp: {0} pressure: {1} altitude: {2}".format(temp, pressure, altitude))
        
        humidity, temp_dht = self.get_humidity()
        temp_dht = self.c_to_f(temp_dht)
        print("humidity: {0} dht temp: {1}".format(humidity, temp_dht))

        query = """INSERT INTO main.measurements (sl_pressure, pressure,
                               temp, altitude_bmp, sea_level_est, humidity, dht_temp) 
                               VALUES (?,?,?,?,?,?,?)"""

        self.c.execute(query, (sl_pressure, pressure, temp, altitude, SLP_EST, humidity, temp_dht))
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    w = Weather()
    w.save_data()

