import numpy as np
import cv2


image = cv2.imread("../images/edge.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 1,                         # 프리윗 수직 마스크y
         -1, 0, 1,
         -1, 0, 1]
data2 = [-1,-1,-1,                         # 프리윗 수평 마스크x
          0, 0, 0,
          1, 1, 1]
mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32).reshape(3, 3)
#형변환 및 saturation 수행
prewitt_x = cv2.convertScaleAbs(cv2.filter2D(gray,-1,mask2))#filter2D 마스크를 적용하는 함수
prewitt_y = cv2.convertScaleAbs(cv2.filter2D(gray,-1,mask1))#convertScaleAbs는 각각의 값을 절대값화시키고 정수화 시키는 작업
prewitt = cv2.addWeighted(prewitt_x,1,prewitt_y,1,0)
cv2.imshow("image", image)
cv2.imshow("prewitt edge", prewitt)
cv2.waitKey(0)
