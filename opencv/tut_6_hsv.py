import cv2
img  = cv2.imread("img/img1.jpg")
img_HSv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV imgage",img_HSv)
cv2.imshow("hue channel", img_HSv[:,:,0])
cv2.imshow("saturation channel", img_HSv[:,:,1])
cv2.imshow("value channel", img_HSv[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()