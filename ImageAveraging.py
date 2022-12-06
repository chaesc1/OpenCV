import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_noise(std,gray):
    height,width = gray.shape
    img_noise = np.zeros((height,width),dtype=np.float64)#노이즈를 만들 빈 이미지 생성

    for i in range(height):
        for j in range(width):
            noise = np.random.normal() #메이크노이즈에 정규분포를 따르는 랜덤한 숫자를 넣음
            set_noise = std * noise
            img_noise[i][j] = gray[i][j] + set_noise

    return img_noise

def run():
    img = cv2.imread("./img/lenna_gray.png")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    height,width = gray.shape

    std = 30

    img_noise = make_noise(std,gray)
    img_noise2 = make_noise(std,gray)
    img_noise3 = make_noise(std, gray)
    img_noise4 = make_noise(std, gray)
    img_noise5 = make_noise(std, gray)
    img_noise6 = make_noise(std, gray)

    out2 = np.zeros((height,width),dtype=np.float64)#두개의 이미지 평균
    out8 = np.zeros((height,width),dtype=np.float64)#3 이미지 평균
    out16 = np.zeros((height,width),dtype=np.float64)#4 이미지 평균
    out32 = np.zeros((height, width), dtype=np.float64)  #5 이미지 평균
    out128 = np.zeros((height, width), dtype=np.float64)  #6

    #평균 계산
    for i in range(height):
        for j in range(width):
            if (img_noise[i][j]+img_noise2[i][j])/2 > 255:
                out2[i][j] = 255
            else:
                out2[i][j] = (img_noise[i][j]+img_noise2[i][j])/2

            if (img_noise[i][j]+img_noise2[i][j] + img_noise3[i][j])/3 > 255:
                out8[i][j] = 255
            else:
                out8[i][j] = (img_noise[i][j]+img_noise2[i][j]+img_noise3[i][j])/3

            if (img_noise[i][j]+img_noise2[i][j] + img_noise3[i][j]+img_noise4[i][j])/4 > 255:
                out16[i][j] = 255
            else:
                out16[i][j] = (img_noise[i][j]+img_noise2[i][j] + img_noise3[i][j]+img_noise4[i][j])/4

            if (img_noise[i][j]+img_noise2[i][j] + img_noise3[i][j]+img_noise4[i][j] + img_noise5[i][j])/5 > 255:
                out32[i][j] = 255
            else:
                out32[i][j] = (img_noise[i][j]+img_noise2[i][j] + img_noise3[i][j]+img_noise4[i][j] + img_noise5[i][j])/5

            if (img_noise[i][j]+img_noise2[i][j]+img_noise3[i][j]+img_noise4[i][j]+img_noise5[i][j]+img_noise6[i][j])/6 >255:
                out128[i][j] = 255
            else:
                out128[i][j] = (img_noise[i][j]+img_noise2[i][j]+img_noise3[i][j]+img_noise4[i][j]+img_noise5[i][j]+img_noise6[i][j])/6
    cv2.imshow("original", gray)
    cv2.imshow('noise', img_noise.astype(np.uint8))
    cv2.imshow('avr2', out2.astype(np.uint8))
    cv2.imshow('avr8', out8.astype(np.uint8))
    cv2.imshow('avr16', out16.astype(np.uint8))
    cv2.imshow('avr32', out32.astype(np.uint8))
    cv2.imshow('avr128', out128.astype(np.uint8))

    cv2.waitKey(0)


run();


