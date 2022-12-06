import cv2
import numpy as np

img = cv2.imread('../lenna.png');
height, width, channel = img.shape

bgr = img.astype(np.float32) / 255.0

b,g,r = cv2.split(bgr)

h = np.zeros((height,width),dtype=np.float32)
s = np.zeros((height,width),dtype=np.float32)
v = np.max(bgr,axis=2)

for i in range(height):
    for j in range(width):
        if v[i][j] == 0: #v가0-> 모든 값이 0인 경우이다.->h,s도 0이 된다.
            h[i][j] = 0
            s[i][j] = 0
        else:
            min_rgb = min(bgr[i][j])

            s[i][j] = 1 - (min_rgb/v[i][j])
            if v[i][j] == r[i][j]:
                h[i][j] = 60 * (g[i][j] - b[i][j]) / (v[i][j] - min_rgb)
            elif v[i][j] == g[i][j]:
                h[i][j] = 120 + (60 * (b[i][j] - r[i][j])) / (v[i][j] - min_rgb)
            elif v[i][j] == b[i][j]:
                h[i][j] = 240 + (60 * (r[i][j] - g[i][j])) / (v[i][j] - min_rgb)
            if h[i][j] < 0:
                h[i][j] += 360
            h[i][j] /= 360

hsv_img = (np.dstack((h,s,v)) * 255).astype(np.uint8)
cv2.imshow("Original",img)
cv2.imshow("h",h)
cv2.imshow("s",s)
cv2.imshow("v",v)
cv2.imshow("hsv",hsv_img)
cv2.waitKey(0)

