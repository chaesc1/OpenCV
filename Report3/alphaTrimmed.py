import cv2
import numpy as np

def salt_pepper_noise(img, n): #소금후추잡음 생성 함수.
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for (x, y) in zip(x, y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255
    return noise


def alpha_trimmed(alpha):#alpha = 0-> maenfilter/alpha = 0.5 -> medianfilter
    img = cv2.imread("../lenna.png", cv2.IMREAD_GRAYSCALE)
    height, width = img.shape

    noise = salt_pepper_noise(img, 10000)

    out = np.zeros((height+1,width+1),dtype = np.float32)
    out[1:1+height, 1:1+width] = img.copy().astype(np.float32)
    temp = out.copy()
    for i in range(height):
        for j in range(width):
            mean = np.sort(np.ravel(temp[i:i+3,j:j+3]))
            out[1+i,1+j] = np.mean(mean[int(alpha * 9):-int(alpha*9)])
            #3*3이라 가정할때 평균을 기준으로 alpha * 9 를 +-한 범위의 평균을 출력영상으로 내보냄
    out = out[1:1+height,1:1+width].astype(np.uint8)

    cv2.imshow("noise",noise)
    cv2.imshow("original",img)
    cv2.imshow("out",out)
    cv2.waitKey(0)

alpha_trimmed(0.3)