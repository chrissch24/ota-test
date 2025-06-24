# Programm: OTA-Test
# Ersteller: Ch.Scheele

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin
import time

firmware_url = "https://raw.githubusercontent.com/chrissch24/ota-test/main"

led1 = Pin(4, Pin.OUT)
led2 = Pin(5, Pin.OUT)

# LED Tester
led1.value(1)
led2.value(1)
time.sleep(0.5)
led1.value(0)
led2.value(0)

# Hauptschleife
while True:
    led1.value(1)
    led2.value(1)
    time.sleep(1)
    led1.value(0)
    led2.value(0)
    time.sleep(2)
