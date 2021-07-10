import cv2
img = cv2.imread("img/img1.jpg")
cv2.imshow("original", img)
resize_img = cv2.resize(img, None, fx=0.75, fy=0.75)
cv2.imshow("original", resize_img)
print(img.shape)
print(resize_img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows