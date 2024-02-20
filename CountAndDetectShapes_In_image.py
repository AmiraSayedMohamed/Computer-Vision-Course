import cv2

triangle_count = 0
cross_count = 0
circle_count = 0
square_count = 0


img = cv2.imread("shapesROV.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    shape = ""

    if len(approx) == 3:
        shape = "Triangle"
        triangle_count += 1
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape = "Square"
            square_count += 1
        else:
            shape = "Rectangle"

    elif len(approx) == 12:
        shape = "Cross"
        cross_count += 1


    elif len(approx) >= 8:
        # Check circularity by verifying contour area and perimeter
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        circularity = 4 * 3.1415 * area / (perimeter * perimeter)
        if circularity > 0.85:
            shape = "Circle"
            circle_count += 1
        else:
            shape = "Cross"
            cross_count += 1

    else:
        shape = "Unknown"

    cv2.drawContours(img , [approx], -1, (77, 0, 255), 4)

#cv2.putText(img, shape, (approx[0][0][0], approx[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
cv2.putText(img, f"Triangle: {triangle_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
cv2.putText(img, f"Cross: {cross_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
cv2.putText(img, f"Square: {square_count}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
cv2.putText(img, f"Circle: {circle_count}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

print("Number of Triangle is: ", triangle_count)
print("Number of Cross is: ", cross_count)
print("Number of square: ", square_count)
print("Number of circle: ", circle_count)
cv2.imshow("image", img)
cv2.waitKey(0)
