import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, Initframe = cap.read()
    frame = cv2.flip(Initframe,1)
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    deep_orange = np.array([10,100, 20])
    bright_orange = np.array([25, 255, 255])
    orange_mask = cv2.inRange(hsv_frame,deep_orange,bright_orange)
    contours,hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)

    for i in contours:
        (x,y,w,h) = cv2.boundingRect(i)


        cv2.rectangle( frame ,(x ,y ), (x + w ,y + h) , ( 0, 255, 0) , 2)
        break

    midpoint = (x + w/2,y + h/2)


    if midpoint[0] > 250 and midpoint[0] < 350 and midpoint[1] > 250 and midpoint[1] < 350:
        image = cv2.putText(frame, "Pick up", (30,100),cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0), 2, cv2.LINE_AA)
    else:
        image = cv2.putText(frame, "Get into position", (30, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.rectangle(frame, (250, 250), (350, 350), (0, 0, 255), 3)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", orange_mask)

    key = cv2.waitKey(1)
    if key == 113:
        break
cap.release()
cv2.destroyAllWindows()
