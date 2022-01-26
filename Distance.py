import RPi.GPIO as GPIO
import time 
    
GPIO.setmode(GPIO.BOARD)

    TRIG = 7
    ECHO = 12

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

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
    
    
    
GPIO.cleanup()
