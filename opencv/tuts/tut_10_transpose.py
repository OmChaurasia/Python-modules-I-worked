import cv2
img = cv2.imread("img/img1.jpg")
cv2.imshow("output", img)

transpose_img =cv2.transpose(img)

cv2.imshow("transpose",transpose_img)

cv2.waitKey(0)
cv2.destroyAllWindows()