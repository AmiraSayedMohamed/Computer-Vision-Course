from matplotlib import pyplot as plt
import cv2

img = cv2.imread("shirt2.jpg")
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()
