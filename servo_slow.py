import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

pwm.set_pwm(0,0,100)
time.sleep(1)

while True:
  for duty in range(100, 561):
    pwm.set_pwm(0,0,duty)
    time.sleep(0.05)
  for duty in range(560, 99, -1):
    pwm.set_pwm(0,0,duty)
    time.sleep(0.05)


  
