import cv2
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)


ENA_L = 40
ENB_L = 38

IN1_L = 37
IN2_L = 36
IN3_L = 35
IN4_L = 33

ENA_R = 32
ENB_R = 31

IN1_R = 29
IN2_R = 22
IN3_R = 18
IN4_R = 16

GPIO.setup(IN1_L,GPIO.OUT)
GPIO.setup(IN2_L,GPIO.OUT)
GPIO.setup(IN3_L,GPIO.OUT)
GPIO.setup(IN4_L,GPIO.OUT)
GPIO.setup(ENA_L,GPIO.OUT)
GPIO.setup(ENB_L,GPIO.OUT)
GPIO.output(IN1_L,GPIO.LOW)
GPIO.output(IN2_L,GPIO.LOW)
GPIO.output(IN3_L,GPIO.LOW)
GPIO.output(IN4_L,GPIO.LOW)

pmwAL = GPIO.PWM(ENA_L,1000)
pmwBL = GPIO.PWM(ENB_L,1000)

GPIO.setup(IN1_R,GPIO.OUT)
GPIO.setup(IN2_R,GPIO.OUT)
GPIO.setup(IN3_R,GPIO.OUT)
GPIO.setup(IN4_R,GPIO.OUT)
GPIO.setup(ENA_R,GPIO.OUT)
GPIO.setup(ENB_R,GPIO.OUT)
GPIO.output(IN1_R,GPIO.LOW)
GPIO.output(IN2_R,GPIO.LOW)
GPIO.output(IN3_R,GPIO.LOW)
GPIO.output(IN4_R,GPIO.LOW)

pmwAR = GPIO.PWM(ENA_R,1000)
pmwBR = GPIO.PWM(ENB_R,1000)

pmwAL.start(75)
pmwBL.start(75)

pmwAR.start(75)
pmwBR.start(75)

def Drive():
    GPIO.output(IN1_L,GPIO.LOW)
    GPIO.output(IN2_L,GPIO.HIGH)
    GPIO.output(IN3_L,GPIO.LOW)
    GPIO.output(IN4_L,GPIO.HIGH)
    GPIO.output(IN1_R,GPIO.LOW)
    GPIO.output(IN2_R,GPIO.HIGH)
    GPIO.output(IN3_R,GPIO.LOW)
    GPIO.output(IN4_R,GPIO.HIGH)
while True:
     Drive()

GPIO.cleanup


    