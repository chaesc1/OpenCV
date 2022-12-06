#이산 푸리에 변환은 원본 신호의 한 원소에 곱하는 기저 함수의 원소들은 원소 길이만큼 반복적으로 곱해지기 때문에 신호가 커질수록 계산 속도는 기하급수적으로 느려짐
#고속 푸리에 변환은 이 과정을 삼각함수의 주기성을 이용해 작은 단위로 반복적으로 분리해서 수행한 후 합하여 효율성을 높이는 방법.

#먼저 푸리에 변환에서 짝수 번째 부분 2n과 홀수번째부분 2n+1을 분리하여 수식을 정리.

import  numpy as np,cv2
from Common.dft2d import exp,calc_spectrum,fftshift
from Common.fft2d import zeropadding

def butterfly(pair,L,N,dir): #L은 전체신호의 절반부만 가져온다.
    for k in range(L):
        Geven, Godd = pair[k],pair[k+L]
        pair[k] = Geven + Godd * exp(dir * k / N)
        pair[k+L] = Geven - Godd * exp(dir * k / N)

def pairing(g,N,dir,start = 0, stride = 1):
    if N == 1: return [g[start]]
    L = N // 2
    sd = stride * 2
    part1 = pairing(g,L,dir,start,sd) #홀수 신호 재귀 분리
    part2 = pairing(g,L,dir,start + stride,sd) #짝수 신호 재귀 분리
    pair = part1 + part2 #재귀 결과 병합
    butterfly(pair,L,N,dir) #버터플라이 수행
    return pair

def fft(g):#고속푸리에 변환
    return pairing(g,len(g),1)

def ifft(g):#고속푸리에 역변환
    fft = pairing(g,len(g),-1)
    return [v / len(g) for v in fft] #실수부만 반환

def fft2(image):
    pad_img = zeropadding(image)
    tmp = [fft(row) for row in pad_img]
    dst = [fft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ifft2(image):
    tmp = [ifft(row) for row in image]
    dst = [ifft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

image = cv2.imread('../images/dft_240.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")
#
dft1 = fft2(image)         # 사용자 구현 fft
spectrum4 = calc_spectrum(dft1)
dft2 = np.fft.fft2(image)
dft3 = cv2.dft(np.float32(image), flags = cv2.DFT_COMPLEX_OUTPUT)

spectrum1 = calc_spectrum(fftshift(dft1))           # 셔플링후 주파수 스펙트럼 영상 생성
spectrum2 = calc_spectrum(fftshift(dft2))           # 주파수 스펙트럼 영상
spectrum3 = calc_spectrum(fftshift(dft3))           # 주파수 스펙트럼 영상

idft1 = ifft2(dft1).real                          # 사용자 구현 2차원 IDFT 수행
idft2 = np.fft.ifft2(dft2).real                    # 내장함수 2차원 IDFT 수행
idft3 = cv2.idft(dft3, flags=cv2.DFT_SCALE)[:,:,0]
#
print("user 방법 변환 행렬 크기:", dft1.shape)
print("np.fft 방법 변환 행렬 크기:", dft2.shape)
print("cv2.dft 방법 변환 행렬 크기:", dft3.shape)
#
cv2.imshow("image", image)
cv2.imshow("fft spectrum1", spectrum4)
cv2.imshow("idft spectrum1", spectrum1)
#cv2.imshow("idft spectrum2-np.fft", spectrum2)
#cv2.imshow("idft spectrum3-OpenCV", spectrum3)
cv2.imshow("idft_img1", cv2.convertScaleAbs(idft1))
cv2.imshow("idft_img2", cv2.convertScaleAbs(idft2))
#cv2.imshow("idft_img3", cv2.convertScaleAbs(idft3))
cv2.waitKey(0)

