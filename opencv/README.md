## Read an image
```
img = cv2.imread(path)
```
## Show an image in a new window
```
cv2.imshow(window_title_name,image)
cv2.waitKey(0)
```
- waitkey is for waiting for a key pressed

## Destroy all Window
```
cv2.destroyAllWindows()
```
## Save an image
```
cv2.imwrite(file_name,image)
```
## Get Shape of image file(height, width, layer)
```
img.shape
```
- This return a tuple `(height, width, layer)`
## Convert image to gray scaled
While reading
```
img = cv2.imread(path,0)
```
After importing
```
gray_img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

## Convert image to binary image
```
ret ,binary_img = cv2.threshold(gray_img,127 ,255, cv2.THRESH_BINARY)
```