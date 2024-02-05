import numpy as np
import cv2

img = cv2.imread('shirt2.jpg')

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 0]
        red = img[y, x, 0]
        mycolorimage = np.zeros((512,512,3), dtype = np.uint8)
        mycolorimage[:] = [blue, green, red]


        cv2.imshow('color', mycolorimage)

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
