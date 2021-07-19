import cv2
import numpy as np
img  = cv2.imread("img/img1.jpg")
draw_img= np.zeros((308,240),dtype=np.uint8)
cv2.rectangle(draw_img,(35,35),(200,200),(255,255,255),2)


def draw_on_image(image, binary_image): 
    contours,h= cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.fillPoly(image,contours,(255,0,0))
    image= cv2.drawContours(image, contours,-1, (255,0,0))
    return image
    
img= draw_on_image(img,draw_img)
cv2.imshow("frame",img)

cv2.waitKey(0)
cv2.destroyAllWindows()