import numpy as np
import cv2

img = np.zeros((700, 500, 3), np.uint8)


cv2.line(img, (0,0), (500, 700), (0, 0, 255), 5)
cv2.rectangle(img, (0, 0), (500, 700), (0, 255, 0), 7)
cv2.circle(img, (250, 350), 70, (255, 255, 0), 6)
cv2.putText(img,"Engineering Society", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0 , 255), 5)

cv2.imshow("img", img)
cv2.waitKey(0)
