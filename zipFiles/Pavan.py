from tracemalloc import start
import cv2 as cv
from cv2 import COLOR_BGR2RGB
# from cv2 import cvtColor
import numpy as np
from matplotlib import pyplot as plt

path=r"C:\Users\91817\Downloads\image1.jpg"

img=cv.imread(path,0)
cv.namedWindow("Gray_image",cv.WINDOW_NORMAL)
cv.imshow("Gray_image",img)
cv.waitKey(0)
cv.destroyAllWindows()


image=cv.imread(path)


image_rgb=cv.cvtColor(image,cv.COLOR_BGR2RGB)
#cv.namedWindow("RGB_image",cv.WINDOW_NORMAL)
# cv.imshow("RGB_image",image_rgb)
start_point=(850,1170)

end_point=(1170,480)

image=cv.rectangle(image_rgb,start_point,end_point,(0,0,255),4)



plt.subplot(1, 1, 1)
plt.imshow(image_rgb)
plt.show()
