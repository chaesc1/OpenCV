import cv2
import numpy as np

image = cv2.imread("../lenna.png",cv2.IMREAD_GRAYSCALE)

#대표적인 라플라시안마스크 필터
data1 = np.array([	[0,		1,		0],  												# 4 방향 필터
			[1, 	-4,		1],
			[0, 	1,		0]])
data2 = np.array([	[-1,	-1,		-1],													# 8 방향 필터
			[-1, 	8, 	    -1],
			[-1, 	-1, 	-1]])
#mask4 = np.array(data1, np.int8)   # 음수가 있으므로 자료형이 int8인 행렬 선언
#mask8 = np.array(data2, np.int8)

# OpenCV 함수 cv2.filter2D() 통한 라플라시안 수행
dst1 = cv2.filter2D(image, -1, data1)
dst2 = cv2.filter2D(image, -1, data2)
dst3 = cv2.Laplacian(image, -1)      # OpenCV 라플라시안 수행 함수

cv2.imshow("image", image)
cv2.imshow("filter2D 4-direction", dst1.astype(np.float32))
cv2.imshow("filter2D 8-direction", dst2.astype(np.float32))
cv2.imshow("Laplacian_OpenCV", dst3.astype(np.float32))
cv2.waitKey(0)

