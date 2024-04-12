


from PIL import Image,ImageFilter
import cv2 
img = cv2.imread ("C:\\Users\\91817\\Downloads\\pexels-irina-iriser-1408221.jpg",1)

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
#print(img.shape)
#print(typr(img))
#print(img)
cv2.imshow("path",resized)
cv2.waitKey(0)
#cv2.destroyAllWindows()


img = cv2.imread ("C:\\Users\\91817\\Downloads\\pexels-irina-iriser-1408221.jpg",255)

resized = cv2.resize(img, (1080,800))
#print(img.shape)

cv2.imshow("path",resized)
cv2.waitKey(0)


