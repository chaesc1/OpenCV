import cv2
import numpy as np

def median():
    img = cv2.imread('../lenna.png')
    height, width, channel = img.shape

    noise = img.copy()
    salt = int(height * width * channel * 0.1)
    for i in range(salt):
        row = int(np.random.randint(99999, size=1) % height)
        col = int(np.random.randint(99999, size=1) % width)
        ch = int(np.random.randint(99999, size=1) % channel)
        noise[row][col][ch] = 255 if np.random.randint(99999, size=1) % 2 == 1 else 0

    out1 = np.zeros((height + 2, width + 2, channel), dtype=np.float32)
    out1[1: 1 + height, 1: 1 + width] = img.copy().astype(np.float32)
    temp1 = out1.copy()

    out2 = np.zeros((height + 4, width + 4, channel), dtype=np.float32)
    out2[2: 2 + height, 2: 2 + width] = img.copy().astype(np.float32)
    temp2 = out2.copy()

    for i in range(height):
        for j in range(width):
            for k in range(channel):
                out1[1 + i, 1 + j, k] = np.median(temp1[i:i + 3, j:j + 3, k])

                hybrid_temp1 = np.median((temp2[i, j, k], temp2[i + 1, j + 1, k], temp2[i + 2, j + 2, k],
                                          temp2[i + 3, j + 3, k], temp2[i + 4, j + 4, k]))
                hybrid_temp2 = np.median((temp2[i + 4, j, k], temp2[i + 3, j + 1, k], temp2[i + 2, j + 2, k],
                                          temp2[i + 1, j + 3, k], temp2[i, j + 4, k]))
                hybrid_temp3 = np.median((temp2[i: i + 5, j:j + 5, k]))
                out2[2 + i, 2 + j, k] = np.median((hybrid_temp1, hybrid_temp2, hybrid_temp3))

    out1 = out1[1:1 + height, 1:1 + width].astype(np.uint8)
    out2 = out2[2:2 + height, 2:2 + width].astype(np.uint8)

    cv2.imshow('original', img)
    cv2.imshow('salt', noise)
    cv2.imshow('median', out1)
    cv2.imshow('hybrid median', out2)
    cv2.waitKey(0)
median()