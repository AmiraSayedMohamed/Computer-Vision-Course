import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Unable to read frame from camera")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # Draw contours only if contours are found
    if contours:
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 4)
        print("Number of contours = " + str(len(contours)))
    
    cv2.imshow('Video Feed', frame)
    
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
