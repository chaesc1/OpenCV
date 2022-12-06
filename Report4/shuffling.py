import cv2
import numpy as np

def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h // 2, w // 2                     # 나누기 하며 소수점 절삭
    dst[h-cy:, w-cx:] = np.copy(img[0:cy , 0:cx ])      # 1사분면 -> 3사분면
    dst[0:cy , 0:cx ] = np.copy(img[h-cy:, w-cx:])      # 3사분면 -> 1사분면
    dst[0:cy , w-cx:] = np.copy(img[h-cy:, 0:cx ])      # 2사분면 -> 4사분면
    dst[h-cy:, 0:cx ] = np.copy(img[0:cy , w-cx:])      # 4사분면 -> 2사분면
    return dst