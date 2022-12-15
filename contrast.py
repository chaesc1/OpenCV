import cv2
import matplotlib.pyplot as plt
import numpy as np

var = 5
img = cv2.imread('lenna.png',cv2.IMREAD_GRAYSCALE)

out = img.copy()
height,width = img.shape#이미지의 크기를 불러옴

high = img.max()
low = img.min()

for i in range(height):
    for j in range(width):
        out[i][j] = ((img[i][j]-low) * 255 / (high - low))#공식new pixel = (old pixel - low) * 255 / high - low

cv2.imshow("Original",img)
cv2.imshow("stretching",out)

cv2.waitKey(0)
