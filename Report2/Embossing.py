import cv2
import numpy as np


img = cv2.imread("../clouds.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask1 = np.array([[-1, 0, 0], [0, 0, 0], [0, 0, 1]]) #음각 마스크
mask2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]) #양각 마스크


out1 = cv2.filter2D(gray, -1, mask1) # filter2d 함수로 영상,-1 -> 원영상과 동일한 타입, 적용할 마스크.
out2 = cv2.filter2D(gray, -1, mask2)
output1= cv2.filter2D(gray, -1, mask1) + 128
output2= cv2.filter2D(gray, -1, mask2) - 128

# uint8 처리
output1[output1 > 255] = 255
output1[output1 < 0] = 0
output1 = np.uint8(output1)

cv2.imshow("original", gray)
cv2.imshow('mask1', output1)
cv2.imshow('mask2', output2)

cv2.waitKey(0)