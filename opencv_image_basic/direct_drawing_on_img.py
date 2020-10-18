#importing files 
import numpy as np
import cv2


#++++++++++++++ Function +++++++++++++++
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 50,(0,255,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,0,0),-1)
 

cv2.namedWindow(winname = 'image_Window')

cv2.setMouseCallback('image_Window', draw_circle)

# create a image of size 512 X 512 
img = np.zeros((512,512,3) )
# ++++++++++ image window +++++++++++++

while True:
    
    cv2.imshow("image_Window",img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

