import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)  # 50Hz

while True:
  pwm.set_pwm(0,0,300)
  time.sleep(1)
  pwm.set_pwm(0,0,400)
  time.sleept(1)
