import uuid      #Unique identifier the purpose of this library to give a unique name for each picture you download
import os        #to change path of the picture
import time
import cv2      # to open your lab camera

os.chdir(r"C:\the\path\for\your\data\that\contain\images\label")  # Path of your data
IMAGES_PATH = os.path.join('data', 'images')  #data/images    #data is folder containg 2 folder images and  labels
labels = ['Car', 'Person', 'cone']


"""
number_imgs = 20 << this mean that  we will get 20 pictures for each class
is you need to increase the accuracy increas the number of imgs
"""
number_imgs = 20   # this mean will get 20 picture for each class
cap = cv2.VideoCapture(0)

for label in labels:
    print("Collecting images for {}".format(label))
    time.sleep(5)  # delay 5 second after finish 1 class to continue to next class

    #loop through image range
    for img_num in range(number_imgs):
        print("Collecting images for {}, image number {}".format(label, img_num))

        # Frames from camera
        ret, frame = cap.read()

        # Naming out image path
        imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')


        # writes our image to file
        cv2.imwrite(imgname, frame)

        #Render to screen
        cv2.imshow("Image Collection", frame)

        # 3 Second delay between captures
        time.sleep(3)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
