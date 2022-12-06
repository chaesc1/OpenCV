#감마보정 공식
#Output = Input^gamma

import numpy as np
import cv2

g = float(input("감마값 : "))

img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

out = gray.copy()
#out = out.astype(np.float64)
#감마보정을 할때 단순히 원래값에 곱하면 안된다.
#감마값에 따라 오버플로우가 발생하게 된다.
#그래서 정규화라는것을 하게 되는데, 정규화는 0-1사이의 값으로 모두 바꿔버리는것이다.
#가장 밝은값이 0,가장어두운값이 255라면 모든 값에 255를 나눠버리면 0-1 사이 값이된다.
out = ((out/255)**(1/g))*255
#g제곱이 아니라 1/g 제곱인 이유는 값이 높아질 수록 밝기가 같이 올라가도록 하기 위해서.

out = out.astype(np.uint8)

cv2.imshow("Original",img)
cv2.imshow("gamma_correction",out)

cv2.waitKey(0)