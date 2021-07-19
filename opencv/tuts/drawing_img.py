import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
# cv2.line(img,(10,10),(500,500),(255,0,0),5)
# cv2.rectangle(img,(50,50),(400,400),(255,0,0),-1)
# cv2.rectangle(img,(50,50),(400,400),(255,0,0),5)
# cv2.circle(img, (200,200),67,(255,0,0),10)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Om Chaurasia",(10,500),font,1,(12,25,175),2)
cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()