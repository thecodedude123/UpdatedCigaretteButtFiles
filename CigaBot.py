import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11, 50)

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

TRIG = 7
ECHO = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

cap = cv2.VideoCapture(0)

def Drive():
    pmwAL.start(75)
    pmwBL.start(75)

    pmwAR.start(75)
    pmwBR.start(75)
    GPIO.output(IN1_L,GPIO.LOW)
    GPIO.output(IN2_L,GPIO.HIGH)
    GPIO.output(IN3_L,GPIO.LOW)
    GPIO.output(IN4_L,GPIO.HIGH)
    GPIO.output(IN1_R,GPIO.LOW)
    GPIO.output(IN2_R,GPIO.HIGH)
    GPIO.output(IN3_R,GPIO.LOW)
    GPIO.output(IN4_R,GPIO.HIGH)
    pmwAL.stop()
    pmwBL.stop()

    pmwAR.stop()
    pmwBR.stop()

while True:
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    distance = round(sig_time / 0.000148,0)

    print('Distance: {} in'.format(distance))
    
    time.sleep(0.1)
    
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    deep_orange = np.array([10,100, 20])
    bright_orange = np.array([25, 255, 255])
    orange_mask = cv2.inRange(hsv_frame,deep_orange,bright_orange)
    _,contours,_ = cv2.findContours(orange_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)

    for i in contours:
        (x,y,w,h) = cv2.boundingRect(i)


        cv2.rectangle( frame ,(x ,y ), (x + w ,y + h) , ( 0, 255, 0) , 2)
        break

    midpoint = (x + w/2,y + h/2)


    if midpoint[0] > 250 and midpoint[0] < 350 and midpoint[1] > 250 and midpoint[1] < 350:
        image = cv2.putText(frame, "Pick up", (30,100),cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0), 2, cv2.LINE_AA)
        pwm.start(0)

        pwm.ChangeDutyCycle(5) # left -90 deg position
        sleep(1)
        pwm.ChangeDutyCycle(7.5) # neutral position
        sleep(1)
        pwm.ChangeDutyCycle(10) # right +90 deg position
        sleep(1)

        pwm.stop()

        
    else:
        image = cv2.putText(frame, "Get into position", (30, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2, cv2.LINE_AA)
        Drive()

    cv2.rectangle(frame, (250, 250), (350, 350), (0, 0, 255), 3)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", orange_mask)

    key = cv2.waitKey(1)
    if key == 113:
        break
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()

