import RPi.GPIO as GPIO
import time

GPIO_PINS = [4, 14, 15, 18, 23, 24, 25]

GPIO.setmode(GPIO.BCM)

for pin in GPIO_PINS:
  GPIO.setup(pin, GPIO.OUT)

try:
  while True:
    for pin in GPIO_PINS:
      GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)

    for pin in GPIO_PINS:
      GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()

