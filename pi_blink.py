import RPi.GPIO as GPIO
import time


# set board mode
# set pin mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)


while True:
    # blink led while raspberry pi is powered on
    GPIO.output(16, True)
    time.sleep(1)
    GPIO.output(16, False)
    time.sleep(1)
