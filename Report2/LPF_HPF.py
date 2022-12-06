import cv2
import numpy as np
import matplotlib.pyplot as plt

def filtering():
    img = cv2.imread('../lenna.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)#원영상을 주파수로 변경.

    row, col = int(height / 2), int(width / 2) #중앙을 찾는 과정.
    LPF = np.zeros((height, width, 2), np.uint8) #원영상과 같은 크기의 zeros 영상 만들어.
    LPF[row - 50:row + 50, col - 50:col + 50] = 1 #LPF 만들기 위해 빈 영상의 중앙에서 가로 세로 각각 +-50범위는 1로 변환
    LPF_shift = dft_shift * LPF #주파수로 변환된 영상과 위의 값을 곱해줘. 그럼 +-50범위만 남게되고 나머지는 0이 된다.
    LPF_ishift = np.fft.ifftshift(LPF_shift)
    LPF_img = cv2.idft(LPF_ishift)
    LPF_img = cv2.magnitude(LPF_img[:, :, 0], LPF_img[:, :, 1])

    HPF = np.ones((height, width, 2), np.uint8)#원본영상과 같은크기로 1로된 배열 생성
    HPF[row - 50:row + 50, col - 50:col + 50] = 0#HPF 만들기 위해 빈 영상의 중앙에서 가로 세로 각각 +-50범위를 0으로
    HPF_shift = dft_shift * HPF
    HPF_ishift = np.fft.ifftshift(HPF_shift)#그럼 +-50범위만 0아되고 나머지는 남게 된다.
    HPF_img = cv2.idft(HPF_ishift)
    HPF_img = cv2.magnitude(HPF_img[:, :, 0], HPF_img[:, :, 1])

    cv2.imshow("original",gray)
    cv2.imshow("LPF",LPF_img)
    cv2.imshow("HPF",HPF_img)
    cv2.waitKey(0)
filtering()