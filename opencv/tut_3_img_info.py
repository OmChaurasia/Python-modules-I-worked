import cv2
img = cv2.imread("img/img1.jpg")
cv2.imshow("output",img)
print(img.shape)
print(f"Height : {img.shape[0]}")
print(f"Width : {img.shape[1]}")
print(f"Layers : {img.shape[2]}")
cv2.waitKey(0)
cv2.destroyAllWindows()