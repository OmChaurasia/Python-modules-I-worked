import cv2
img = cv2.imread("img/img1.jpg")
cv2.imshow("output window",img)
cv2.imwrite("Output.jpg",img)


cv2.waitKey(0)
cv2.destroyAllWindows()