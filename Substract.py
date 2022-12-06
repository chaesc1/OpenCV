import cv2

img1 = cv2.imread("./Lenna.png")
img2 = cv2.imread("./peppers.png")

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

height,width = gray1.shape
minus = gray1.copy()

for i in range(width):
    for j in range(height):
        minus[i][j] = int(gray1[i][j]) - int(gray2[i][j])

        if minus[i][j] < 0:
            minus[i][j] = 0

subtract = cv2.subtract(gray1,gray2)#cv2내장 함수로
cv2.imshow('lenna',gray1)
cv2.imshow('peppers',gray2)
cv2.imshow('minus',minus)
cv2.imshow('substract_func',subtract)
cv2.waitKey(0)