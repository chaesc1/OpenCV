import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

histogram, bin = np.histogram(img.ravel(),256,[0,256])
#히스토그램함수를 이용. numpy모듈에 있는 histogram이라는 함수.
cumsum = histogram.cumsum()#히스토그램의 누적합 cumsum은 누적합구할때 씀
print('cumsum',cumsum)

#print(np.uint8((cumsum-cumsum.min() ) * 255/(cumsum.max()-cumsum.min())))
LUT = np.uint8((cumsum-cumsum.min()) * 255/(cumsum.max()-cumsum.min()))#직접계산한 부분.누적합 * 최대화소 / 크기
#값은 정수여야 함으로 int형으로 형변환.

equ = LUT[gray]

hist = cv2.equalizeHist(gray)

cv2.imshow("Original",gray)
cv2.imshow("result",equ)#직접계산
cv2.imshow("result2",hist)#함수로 계산



plt.figure()
plt.subplot(1,3,1)
plt.hist(img.ravel(),256,[0,256])
plt.subplot(1,3,2)
plt.hist(equ.ravel(),256,[0,256])
plt.subplot(1,3,3)
plt.hist(hist.ravel(),256,[0,256])
plt.show()