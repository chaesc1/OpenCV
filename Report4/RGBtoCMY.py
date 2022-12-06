import cv2
import numpy as np

def rgb2cmy():
    img = cv2.imread("../lenna.png")
    bgr = img.astype(np.float32)/255.0
    
    k = 1 - np.max(bgr,axis = 2)
    c = (1 - bgr[...,2] - k) / (1 - k)
    m = (1 - bgr[..., 1] - k) / (1 - k)
    y = (1 - bgr[..., 0] - k) / (1 - k)

    cmyk = (np.dstack((c,m,y,k)) * 255).astype(np.uint8)

    cv2.imshow('Original',img)
    cv2.imshow('b',bgr[..., 0])
    cv2.imshow('g', bgr[..., 1])
    cv2.imshow('r', bgr[..., 2])
    cv2.imshow('c',c)
    cv2.imshow('m',m)
    cv2.imshow('y',y)
    cv2.imshow('k',k)
    cv2.imshow('cmyk',cmyk)
    cv2.waitKey(0)

rgb2cmy()
