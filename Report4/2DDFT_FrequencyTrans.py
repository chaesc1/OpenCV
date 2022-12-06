import numpy as np, cv2, math
from Common.dft2d import dft, idft, calc_spectrum, fftshift

def exp(knN):
    th = -2 * math.pi * knN
    return complex(math.cos(th), math.sin(th))

def dft(g):
    N = len(g)
    dst = [sum((g[n] * exp(k*n/N ) for n in range(N))) for k in range(N) ]  #내부 포문에서 sum함수로 계수 g[n]와 복소수 함소의 곱들을 합하고 외부 포문에서 계수가 가중된 신호를 리스트로 구성
    return np.array(dst)
#1차원 dft수행후 전치시켜서 다시 1차원 dft를 수행하여 전치시켜 다시 1차워 dft를 수행해서 2차 dft
def dft2(image):
    tmp = [dft(row) for row in image] #image행렬을 1행 순회하여 1차원 푸리에 변환을 수행해서 risk 구성
    dst = [dft(row) for row in np.transpose(tmp)] #transpose로 전치 시켜줌
    return np.transpose(dst)                   # 전치 환원 후 반환

def idft(g):
    N = len(g)
    dst = [sum((g[n] * exp(-k*n/ N) for n in range(N))) for k in range(N) ] #k인수에 음수를 곱해서 음수값을 표현
    return np.array(dst) / N #합해진 신호를 전체 길이로 나누어 주었다.

#푸리에 역변환 수행
def idft2(image):
    tmp = [idft(row) for row in image]
    dst = [idft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)                   # 전치 환원 후 반환


image = cv2.imread('../images/dft_128.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")


dft = dft2(image)# 2차원 행렬 image에 2차원푸리에변환 수행 -> 결과는 복소수 return
spectrum1 = calc_spectrum(dft)        # 주파수 스펙트럼 영상 // 복소수행렬의 스펙트럼 크기를 계산하여 행렬로 반환
spectrum2 = fftshift(spectrum1)       # 셔플링 수행해
idft = idft2(dft).real                # 2차원 IDFT 수행해서 영상을 복원시켜
dftImg = dft.real

cv2.imshow("image", image)
cv2.imshow("spectrum1", spectrum1)
cv2.imshow("spectrum2", spectrum2)
cv2.imshow("dft_img",cv2.convertScaleAbs(dftImg))
cv2.imshow("idft_img", cv2.convertScaleAbs(idft))
cv2.waitKey(0)
