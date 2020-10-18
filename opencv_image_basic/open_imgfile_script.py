import cv2

img = cv2.imread('data/3.jpg') # Reading the image using cv2

while True:
    
    cv2.imshow('corona',img) # showing the image
    if cv2.waitKey(1) & 0xFF == 27: #condition wait for 1 milisec and check for Esc button is clicked or not.
        break

cv2.destroyAllWindows()  # destroy all the windows     
