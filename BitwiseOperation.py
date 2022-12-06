import cv2
import numpy as np
img1 = cv2.imread("./Lenna.png")
img2 = cv2.imread("./peppers.png")

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

bit_and = cv2.bitwise_and(gray1,gray2)
bit_or  = cv2.bitwise_or(gray1,gray2)
bit_not = cv2.bitwise_not(gray1)
bit_xor = cv2.bitwise_xor(gray1,gray2)

cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not",bit_not)

cv2.waitKey(0)