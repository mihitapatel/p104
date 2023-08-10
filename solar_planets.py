import cv2 

img = cv2.imread("psolor-system.jpg")

cv2.imshow("output",img)

#gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#cv2.imshow("Gray Image", gray_img)

cv2.waitKey(0)