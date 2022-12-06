import cv2
import numpy as np

src = cv2.imread("../lenna.png",cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit(0)

blr = cv2.GaussianBlur(src, (0, 0), 2)  # 표준편차 2, 필터 크기는 자동 설정

a = 2.0  # 샤프닝 정도 결정하는 변수
dst = np.clip((1+a)*src - a * blr, 0, 255).astype(np.uint8) # 계산은 정수, 출력은 실수

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()