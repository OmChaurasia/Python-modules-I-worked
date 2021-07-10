import cv2
import mediapipe as mp
import time

from mediapipe.python.solutions import hands

vid= cv2.VideoCapture(0)
mpHands= mp.solutions.hands
hands= mpHands.Hands()
mpDraw= mp.solutions.drawing_utils

pTime=0
cTime=0

while True:
    ret, frame= vid.read()
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

    cv2.imshow("frame", frame)
    keyPressed = cv2.waitKey(10)
    if keyPressed == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()