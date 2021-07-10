
import cv2
vid = cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while(True):
    # reading the frame
    ret, frame = vid.read()

    # detecting the face
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)

        # name batch
        linestart=(int(x+w/2),int(y-5))
        lineend=(int(x+w/2),int(y-30))
        # print(linestart)
        cv2.line(frame,linestart,lineend,(255,123,23),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,"Person is here",(x,y-35),font,0.6,(255,123,23),2)


    # key handling
    cv2.imshow('frame', frame)
    key = cv2.waitKey(10) 
    if key == ord('q'):
        break
    elif key == ord('c'):
        cv2.imwrite("Output.jpg",frame)
    else:
        pass
    
vid.release()
cv2.destroyAllWindows()