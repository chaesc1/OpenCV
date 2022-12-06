#5*5를  중앙 픽셀 포함 8개 영역으로 나눔
import cv2
import numpy as np

def nagao():
    img = cv2.imread('../lenna.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    img_noise = np.zeros_like(gray)
    for i in range(height):
        for j in range(width):
            make_noise = np.random.normal()
            set_noise = 10 * make_noise
            img_noise[i][j] = gray[i][j] + set_noise

    out = np.zeros((height + 4, width + 4), dtype=np.float32)
    out[2: 2 + height, 2: 2 + width] = img_noise.copy().astype(np.float32)

    for i in range(height):
        for j in range(width):
            point1 = np.ravel(out[i + 1:i + 4, j:j + 2])
            point1 = np.append(point1, out[i + 2, j + 2])

            point2 = np.ravel(out[i + 3:i + 5, j + 1:j + 4])
            point2 = np.append(point2, out[i + 2, j + 2])

            point3 = np.ravel(out[i + 1:i + 4, j + 3:j + 5])
            point3 = np.append(point3, out[i + 2, j + 2])

            point4 = np.ravel(out[i:i + 2, j + 1:j + 4])
            point4 = np.append(point4, out[i + 2, j + 2])

            point5 = np.ravel(out[i:i + 2, j:j + 2])
            point5 = np.append(point5, out[i + 2, j + 1])
            point5 = np.append(point5, out[i + 1, j + 2])
            point5 = np.append(point5, out[i + 2, j + 2])

            point6 = np.ravel(out[i + 3:i + 5, j:j + 2])
            point6 = np.append(point6, out[i + 2, j + 1])
            point6 = np.append(point6, out[i + 3, j + 2])
            point6 = np.append(point6, out[i + 2, j + 2])

            point7 = np.ravel(out[i + 3:i + 5, j + 3:j + 5])
            point7 = np.append(point7, out[i + 2, j + 3])
            point7 = np.append(point7, out[i + 3, j + 2])
            point7 = np.append(point7, out[i + 2, j + 2])

            point8 = np.ravel(out[i:i + 2, j + 3:j + 5])
            point8 = np.append(point8, out[i + 1, j + 2])
            point8 = np.append(point8, out[i + 2, j + 3])
            point8 = np.append(point8, out[i + 2, j + 2])

            if min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point1):
                out[2 + i, 2 + j] = np.mean(point1)
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point2):
                out[2 + i, 2 + j] = np.mean(point2)
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point3):
                out[2 + i, 2 + j] = np.mean(point3)
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point4):
                out[2 + i, 2 + j] = np.mean(point4)
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point5):
                out[2 + i, 2 + j] = np.mean(point5)
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point6):
                out[2 + i, 2 + j] = np.mean(point6)
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point7):
                out[2 + i, 2 + j] = np.mean(point7)
            elif min(np.var(point1), np.var(point2), np.var(point3), np.var(point4), np.var(point5), np.var(point6), np.var(point7), np.var(point8)) == np.var(point8):
                out[2 + i, 2 + j] = np.mean(point8)

    out = out[2:2 + height, 2:2 + width].astype(np.uint8)
    cv2.imshow('original', gray)
    cv2.imshow('noise', img_noise)
    cv2.imshow('out', out)
    cv2.waitKey(0)

nagao()