import RPi.GPIO as GPIO
import time

ledPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        GPIO.output(ledPin, True)
        print("Led ON")
        time.sleep(1)
        GPIO.output(ledPin, False)
        print("Led OFF")
        time.sleep(1)
except KeyboardInterrupt:
    print("Exit pressed keyboard")
finally:
    GPIO.cleanup()
    print("End")
