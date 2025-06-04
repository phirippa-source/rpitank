import RPi.GPIO as GPIO
import time

Tr = 11 # The pin number of the input end of  the ultrasonic module
Ec = 8  # Pin number of the output end of the ultrasonic module

GPIO.setmode(GPIO.BCM)
GPIO.setup(Tr, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Ec, GPIO.IN)

def measure_dist():
  GPIO.output(Tr, GPIO.HIGH)
  time.sleep(0.000010)            # 10[micro second]
  
  GPIO.output(Tr, GPIO.LOW)
  while not GPIO.input(Ec):       # When the module no longer receives the inital sound wave
    pass
  
  time1 = time.time()             # Write down the time when the initial sound wave emitted
  while GPIO.input(Ec):           # When the module receives the return sound wave.
    pass
  time2 = time.time()             # Write down the time when the return sound wave was captured.

  duration = time2 - time1
  return round( 340 * duration / 2, 2 )


for i in range(20):
  print(measure_dist(), '[m]')
  time.sleep(1)
