import cv2
import numpy as np

def kuwahara():
    img = cv2.imread("../lenna.png")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    height,width = gray.shape

    img_noise = np.zeros_like(gray)
    for i in range(height):
        for j in range(width):
            make_noise = np.random.normal()
            set_noise = 10 * make_noise
            img_noise[i][j] = gray[i][j] + set_noise

    temp = np.zeros((height + 4, width + 4), dtype=np.float32)
    temp[2: 2 + height, 2: 2 + width] = img_noise.copy().astype(np.float32)
    out = np.zeros_like(gray)

    for i in range(height):
        for j in range(width):
            point1 = temp[i:i + 3, j:j + 3]
            point2 = temp[i + 2:i + 5, j:j + 3]
            point3 = temp[i:i + 2, j + 2:j + 5]
            point4 = temp[i + 2:i + 5, j + 2:j + 5]

            if min(np.var(point1), np.var(point2), np.var(point3), np.var(point4)) == np.var(point1):
                out[i, j] = np.mean(temp[i:i + 3, j:j + 3])
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4)) == np.var(point2):
                out[i, j] = np.mean(temp[i + 2:i + 5, j:j + 3])
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4)) == np.var(point3):
                out[i, j] = np.mean(temp[i:i + 2, j + 2:j + 5])
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4)) == np.var(point4):
                out[i, j] = np.mean(temp[i + 2:i + 5, j + 2:j + 5])

    cv2.imshow('original', gray)
    cv2.imshow('noise', img_noise)
    cv2.imshow('out', out.astype(np.uint8))
    cv2.waitKey(0)

kuwahara()