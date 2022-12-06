import cv2
import numpy as np

image = cv2.imread("../images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 1,                  # 수평 마스크
         -2, 0, 2,
         -1, 0, 1]
data2 = [-1,-2,-1,                 # 수직 마스크
          0, 0, 0,
          1, 2, 1]

mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32).reshape(3, 3)

# OpenCV 제공 소벨 에지 계산
sobel_x = cv2.convertScaleAbs(cv2.filter2D(image, -1, mask1))#마스크 적용후 각각의 값 절대값화 후 정수화
sobel_y = cv2.convertScaleAbs(cv2.filter2D(image, -1, mask2))#이미지 정상출력하기 위해.
sobel = cv2.addWeighted(sobel_x, 1, sobel_y, 1, 0)#각각 x와y값을 이미지로 합쳐준다.
cv2.imshow("edge- sobel edge", image)
cv2.imshow("dst- sobel edge", sobel)

cv2.waitKey(0)