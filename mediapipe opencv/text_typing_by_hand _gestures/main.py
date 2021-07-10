import cv2
import numpy as np
import mediapipe as mp
import time
from mediapipe.python.solutions import hands


# vid = cv2.VideoCapture("http://192.168.43.1:4747/mjpegfeed")
vid = cv2.VideoCapture(0)
mpHands= mp.solutions.hands
hands= mpHands.Hands(min_detection_confidence=0.8,
    min_tracking_confidence=0.5)
mpDraw= mp.solutions.drawing_utils

pTime=0
cTime=0

while True:
    ret, frame =vid.read()
    frame=cv2.flip(frame,1)

    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c= frame.shape
                cx,cy= int(lm.x*w), int(lm.y*h)
                # print(id,cx,cy)
                # to check the id of a point 
                if id ==8:
                    cv2.circle(frame,(cx,cy),10,(255,0,0),-1)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


    # fps tracking
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(frame,str(int(fps)), (10,70),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)



    cv2.imshow("camera window",frame)



    key_detection_value = cv2.waitKey(10)
    if key_detection_value == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()