import RPi.GPIO as GPIO
import time

Motor_A_EN    = 17  # Enable B of L298P
Motor_A_Pin1  = 27  # IN3 of L298P
Motor_A_Pin2  = 18  # IN4 of L298P

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Motor_A_EN, GPIO.OUT)
GPIO.setup(Motor_A_Pin1, GPIO.OUT)
GPIO.setup(Motor_A_Pin2, GPIO.OUT)

GPIO.output(Motor_A_Pin1, GPIO.HIGH)
GPIO.output(Motor_A_Pin2, GPIO.LOW)

pwm = GPIO.PWM(Motor_A_EN, 100)
pwm.start(0)
pwm.ChangeDutyCycle(100)

try:
  while True:
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
    

