import cv2
import matplotlib.pyplot as plt


global = aasd
img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

height,width = gray.shape

min = gray.min()
max = gray.max()
out = gray.copy()

low = int(input("하한값 : "))
high = int(input("상한값 : "))
#엔드인 기법은 하한값과 상한값을 정해두고 하한값 미만의 값은 0,상한값 초과하는 값은 255로 변환하고
#나머지 값들은 스트레칭 공식을 적용함

for i in range(width):
    for j in range(height):
        if gray[i][j] < min:#하한값보다 작으면
            out[i][j] = 0
        if gray[i][j] > max:
            out[i][j] = 255
        else:
            out[i][j] = ((gray[i][j] - min) * 255) / (max - min)

cv2.imshow("Original",gray)
cv2.imshow("end_in",out)

cv2.waitKey(0)
