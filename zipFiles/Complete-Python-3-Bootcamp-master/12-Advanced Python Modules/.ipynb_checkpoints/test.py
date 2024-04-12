import cv2 as cv
import numpy as np

video_path = r

cap = cv.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Video end... (OR) error when video running")
        break

    cv.imshow("Frame",frame)
    key = cv.waitKey(25)
    if key == 27:
        break
cap.release 
cv.destroyAllWindows()