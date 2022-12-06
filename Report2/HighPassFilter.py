import cv2
import numpy as np

image = cv2.imread("../Lenna.png", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1/9, -1/9, -1/9,
         -1/9, 8/9, -1/9,
         -1/9, -1/9, -1/9]
mask1 = np.array(data1, np.float32).reshape(3, 3)
hpf = cv2.filter2D(image,-1,mask1)
cv2.imshow("Original",image)
cv2.imshow("HPF",hpf)
cv2.waitKey(0)