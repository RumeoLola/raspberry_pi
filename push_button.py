import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.IN)


while True:
    # blink while on
    GPIO.output(16, True)
    time.sleep(1)
    GPIO.output(16, False)
    time.sleep(1)
    # blink if button is pressed
    if (GPIO.input(18)):
        GPIO.output(16, True)
    else:
        GPIO.output(16, False)
