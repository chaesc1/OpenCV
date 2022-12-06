import cv2
import numpy as np

img = cv2.imread("../lenna.png")
height,width,channel = img.shape
b = img[...,0]
g = img[...,1]
r = img[...,2]
#bgr로 나눠

y = np.zeros((height,width), dtype=np.float32)
cr = np.zeros((height,width), dtype=np.float32)
cb = np.zeros((height,width), dtype=np.float32)
#빈 영상 생성

for i in range(height):
    for j in range(width):
        y[i][j] = 0.299*r[i][j] + 0.587*g[i][j] + 0.144 * b[i][j]
        cr[i][j] = (r[i][j] - y[i][j]) * 0.713 + 128
        cb[i][j] = (b[i][j] - y[i][j]) * 0.564 + 128
#변환공식 이용
out = (np.dstack((y,cr,cb))).astype(np.uint8)
cv2.imshow("original",img)
cv2.imshow("ycbcr",out)
cv2.waitKey(0)