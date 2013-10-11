import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

for i in range(0, 50):
    time.sleep(0.05)
    GPIO.output(15, GPIO.HIGH)

    time.sleep(0.05)
    GPIO.output(15, GPIO.LOW)

GPIO.cleanup()
