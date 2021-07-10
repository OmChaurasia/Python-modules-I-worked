import cv2
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("img/img1.jpg")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
    linestart=(int(x+w/2),int(y-5))
    lineend=(int(x+w/2),int(y-30))
    print(linestart)
    cv2.line(img,linestart,lineend,(255,123,23),2)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"Om Chaurasia",(x,y-35),font,0.6,(255,123,23),2)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()