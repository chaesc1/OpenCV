import cv2
import numpy as np

image = cv2.imread("../images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 0,
         0, 1, 0,
         0, 0, 0]
data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]
mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32).reshape(3, 3)

roberts_x = cv2.convertScaleAbs(cv2.filter2D(image, -1, mask1))#마스크 적용후 각각의 값 절대값화 후 정수화
roberts_y = cv2.convertScaleAbs(cv2.filter2D(image, -1, mask2))#이미지 정상출력하기 위해.
roberts = cv2.addWeighted(roberts_x, 1, roberts_y, 1, 0)#각각 x와y값을 이미지로 합쳐준다.

cv2.imshow("image", image)
cv2.imshow("roberts edge", roberts)

cv2.waitKey(0)