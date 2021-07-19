from typing import Counter
import cv2
import numpy as np

hand = cv2.imread("img/capture.jpg",0)

ret, the = cv2.threshold(hand,70 , 255,cv2.THRESH_BINARY)
contours,b = cv2.findContours(the.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
hull = [cv2.convexHull(c) for c in contours]
# print(hull)
final= cv2.drawContours(hand, hull,-1, (255,0,0))
# cv2.imshow("img",hand)
cv2.imshow("thresh", the)
cv2.imshow("final", final)
cv2.waitKey(0)
cv2.destroyAllWindows()