import pyautogui
import cv2
import numpy as np

screensize = (1366,768)
fourcc= cv2.VideoWriter_fourcc(*"XVID")
output= cv2.VideoWriter("output.avi",fourcc,20.0,(screensize))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen", frame)
    output.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break
    


cv2.destroyAllWindows()