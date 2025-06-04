import RPi.GPIO as GPIO
import time

Motor_A_EN    = 17  # Enable B of L298P
Motor_A_Pin1  = 27  # IN3 of L298P
Motor_A_Pin2  = 18  # IN4 of L298P

Motor_B_EN    = 4  # Enable B of L298P
Motor_B_Pin1  = 14  # IN1 of L298P
Motor_B_Pin2  = 15  # IN2 of L298P

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Moter_A_EN,   GPIO.OUT)
GPIO.setup(Motor_A_Pin1, GPIO.OUT)
GPIO.setup(Motor_A_Pin2, GPIO.OUT)
GPIO.setup(Moter_B_EN,   GPIO.OUT)
GPIO.setup(Motor_B_Pin1, GPIO.OUT)
GPIO.setup(Motor_B_Pin2, GPIO.OUT)

GPIO.output(Motor_A_Pin1, GPIO.HIGH)
GPIO.output(Motor_A_Pin2, GPIO.LOW)
GPIO.output(Motor_B_Pin1, GPIO.HIGH)
GPIO.output(Motor_B_Pin2, GPIO.LOW)

pwmA = GPIO.PWM(Motor_A_EN, 100)
pwmB = GPIO.PWM(Motor_B_EN, 100)
pwmA.start(0)
pwmB.start(0)
pwmA.ChangeDutyCycle(100)
pwmB.ChangeDutyCycle(100)

try:
  while True:
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
