import cv2

img = cv2.imread("camera7.bmp")

out = img.copy()

out = 255-out

cv2.imshow("Original",img)
cv2.imshow("flip",out)
cv2.waitKey(0)