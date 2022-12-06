import cv2
import numpy as np

alpha = float(input("input alpha"))

#합성할 이미지 두개
f1 = cv2.imread("./yate.jpg")
f2 = cv2.imread("./wing_wall.jpg")

#수식 계산해서 직접 알파블렌딩 적용
blend = alpha*f1 + (1-alpha)*f2
blend = blend.astype(np.uint8) #소수점 발생 방지

cv2.imshow('yate.jpg',f1)
cv2.imshow('wing_wall.jpg',f2)
cv2.imshow('alpha*f1 + (1-alpha)*f2',blend)

cv2.waitKey(0)