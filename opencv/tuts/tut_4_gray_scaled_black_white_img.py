# Method 1:

# import cv2
# img = cv2.imread("img/img1.jpg")
# cv2.imshow("output",img)
# gray_img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray image", gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Method 2:

import cv2
img = cv2.imread("img/img1.jpg",0)
cv2.imshow("gray img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()