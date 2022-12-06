import numpy as np, cv2
def make_noise(std,gray):
    height,width = gray.shape
    img_noise = np.zeros((height,width),dtype=np.float64)#노이즈를 만들 빈 이미지 생성

    for i in range(height):
        for j in range(width):
            noise = np.random.normal() #메이크노이즈에 정규분포를 따르는 랜덤한 숫자를 넣음
            set_noise = std * noise
            img_noise[i][j] = gray[i][j] + set_noise

    return img_noise
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
std = 10
img_noise = make_noise(std,image)
ksize = (5, 17)                                        # 크기는 가로x세로로 표현
gaussian_2d = getGaussianMask(ksize, 0, 0)
gaussian_1dX = cv2.getGaussianKernel(ksize[0], 0, cv2.CV_32F)   # 가로 방향 마스크 cv2.CV_32F는 데이타 타입
gaussian_1dY = cv2.getGaussianKernel(ksize[1], 0, cv2.CV_32F)   # 세로 방향 마스크 플롯형

gauss_img1 = cv2.filter2D(img_noise, -1, gaussian_2d)     # 사용자 생성 마스크 적용
gauss_img2 = cv2.GaussianBlur(image, (0,0), 10.7, 1.3) #opencv 제공 함수
#src:원본영상 dst:출력영상 ksize:가우시안 커널 크기(0,0)이면 시그마값에 의해 결정 sigmaX:x방향 sigma sigmaY:y방향 sigma
gauss_img3 = cv2.sepFilter2D(image, -1, gaussian_1dX, gaussian_1dY) #opencv 제공 함수 이용2

cv2.imshow("original",image)
cv2.imshow("noise",img_noise.astype(np.uint8))
cv2.imshow("LPF",gauss_img1.astype(np.uint8))

cv2.waitKey(0)
