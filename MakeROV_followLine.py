#Code to follow line in ROV mission:
import cv2
import numpy as np

# Function to control ROV movement
class ROV:
    def move_forward(self, speed):
        print(f"Moving ROV forward with speed {speed}")

    def move_backward(self, speed):
        print(f"Moving ROV backward with speed {speed}")

    def turn_left(self, angle):
        print(f"Turning ROV left with angle {angle}")

    def turn_right(self, angle):
        print(f"Turning ROV right with angle {angle}")


# Function to detect and follow the red line
def follow_red_line():
    cap = cv2.VideoCapture(0)  # Initialize webcam

    # Initialize ROV control
    rov = ROV()

    while True:
        ret, frame = cap.read()  # Read a frame from the webcam
        if not ret:
            break

        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define range of red color in HSV
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])

        # Threshold the HSV image to get only red colors
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # Find contours in the masked image
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # If contours are found
        if contours:
            # Calculate centroid of the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                red_line_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                frame_center = (frame.shape[1] // 2, frame.shape[0] // 2)  # Calculate frame center

                # Calculate horizontal offset of the red line center from the frame center
                offset = red_line_center[0] - frame_center[0]

                # Adjust ROV movement based on the offset
                if offset < -50:  # If red line is too much to the left
                    print("Move ROV right")
                    rov.turn_right(abs(offset) * 0.1)  # Adjust the scaling factor as needed
                elif offset > 50:  # If red line is too much to the right
                    print("Move ROV left")
                    rov.turn_left(offset * 0.1)  # Adjust the scaling factor as needed
                else:
                    print("ROV aligned with the red line")
                    rov.move_forward(50)  # Example: Move forward with a speed of 50 (adjust as needed)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Main function
if name == "main":
    follow_red_line()
