import cv2
img=cv2.imread("img/img1.jpg")

h,w= img.shape[:2]
rotational_matrix = cv2.getRotationMatrix2D((w/2,h/2),90,0.5)
rotational_image = cv2.warpAffine(img,rotational_matrix,(w,h))
cv2.imshow("rotationimg", rotational_image)

cv2.waitKey(0)
cv2.destroyAllWindows()