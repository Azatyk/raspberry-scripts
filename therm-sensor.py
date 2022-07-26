from w1thermsensor import W1ThermSensor
import time

sensor = W1ThermSensor()

try:
    while True:
        temp = sensor.get_temperature()
        print(temp)
        time.sleep(1)
except KeyboardInterrupt:
    print("Exit pressend keyboard")
finally:
    print("End")
