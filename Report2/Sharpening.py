import numpy as np
import cv2

image = cv2.imread("../images/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# 샤프닝 마스크 원소 지정
data1 = np.array([1, -2, 1,
        -2, 5, -2,
         1, -2, 1])
data2 = np.array([[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]])


sharpening_out1 = cv2.filter2D(image, -1, data1)
sharpening_out2 = cv2.filter2D(image, -1, data2)

cv2.imshow("image", image)
cv2.imshow('sharpening1',sharpening_out1)
cv2.imshow('sharpening2',sharpening_out2)
cv2.waitKey(0)
