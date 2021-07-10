import cv2


# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
# download droidcam in your phone 
url = "http://192.168.43.1:4747/mjpegfeed"
vid = cv2.VideoCapture(url)
# While loop to continuously fetching data from the Url
while True:
	ret, frame = vid.read()

	cv2.imshow("Android_cam", frame)

	# Press Esc key to exit
	key=cv2.waitKey(10)
	if key == ord('q'):
		break
	elif key == ord('c'):
		cv2.imwrite("Output.jpg",frame)
	else:
		pass
cv2.destroyAllWindows()
