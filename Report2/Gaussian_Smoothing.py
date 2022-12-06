import numpy as np, cv2

def getGaussianMask(ksize, sigmaX, sigmaY):
    sigma = 0.3 * ((np.array(ksize) - 1.0) * 0.5 - 1.0) + 0.8  # 표준 편차
    if sigmaX <= 0: sigmaX = sigma[0] #표준편차 양수 아닐 때
    if sigmaY <= 0: sigmaY = sigma[1] #ksize로 기본 표준편차 계산

    u = np.array(ksize)//2 #커널 크기 절반
    x = np.arange(-u[0], u[0]+1, 1) #x방량 범위
    y = np.arange(-u[1], u[1]+1, 1) #y방향 범위
    x, y = np.meshgrid(x, y) #좌표 행렬 생성

    ratio = 1 / (sigmaX*sigmaY * 2 * np.pi)
    v1 = x ** 2 / (2 * sigmaX ** 2)
    v2 = y ** 2 / (2 * sigmaY ** 2 )
    mask = ratio * np.exp(-(v1+v2))#2차원 정규분포수식
    return mask / np.sum(mask)# 원소 전체 합 1 유지.

image = cv2.imread("../images/smoothing.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

ksize = (5, 17)                                        # 크기는 가로x세로로 표현
gaussian_2d = getGaussianMask(ksize, 0, 0)

gauss_img1 = cv2.filter2D(image, -1, gaussian_2d)     # 사용자 생성 마스크 적용


titles = ['image','gauss_img1']
[cv2.imshow(t, eval(t)) for t in titles]
cv2.waitKey(0)
