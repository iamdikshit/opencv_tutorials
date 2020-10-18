
import cv2
import matplotlib.pyplot as plt
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray_frame)
    dst = cv2.cornerHarris(src = gray, blockSize = 2, ksize = 3 , k = 0.04)
    dst = cv2.dilate(dst,None)
    frame[dst > 0.01 * dst.max()] = [0,0,255]
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()





