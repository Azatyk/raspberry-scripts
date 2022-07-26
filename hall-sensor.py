import RPi.GPIO as GPIO
import time

sensorPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)

try:
    while True:
        print(GPIO.input(sensorPin))
        time.sleep(1)
except KeyboardInterrupt:
    print("Exit pressed keyboard")
finally:
    print("End")
