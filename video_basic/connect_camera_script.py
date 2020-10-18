
import cv2

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	cv2.imshow('frame',gray) #video will display in grayscale

	if cv2.waitKey(1) & 0xFF == 27:
		break

capture.release()
cv2.destroyAllWindows()