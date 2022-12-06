import numpy as np,cv2
from Common.interpolation import scaling #interpolation 모듈의 scailing 함수를 임포트

#그냥 간단하게 목적 화소의 좌표를 반올림하는 간단한 알고리즘은 쉽고 빠르지만 모서리 부분에 계단현상이 발생한다.
#그래서 역방향 사상 방법을 적용하여 최근접 이웃 보간법을 수행한다.

#역변환 수식 -> y = y' / ratioY, x = x' / ratioX
def scailing_nearest(img,size): #크기변경함수
    dst = np.zeros(size[::-1], img.dtype) #행렬과 크기는 원소가 역순이다.
    ratioY,ratioX = np.divide(size[::-1],img.shape[:2])#변경 크기 비율/ size를 width와 height으로 나눠 각각 저장
    i = np.arange(0,size[1],1)#목적영상의 세로(i)
    j = np.arange(0,size[0],1)#목적영상의 가로(j)
    i,j = np.meshgrid(i,j) #격자 그리드 생성

    y,x = np.int32(i/ratioY),np.int32(j/ratioX) #입력 영상 좌표
    dst[i,j] = img[y,x]
    return dst

def scaling(img, size):                                # 크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)               # 행렬과 크기는 원소가 역순/
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])#변경 크기 비율/ size를 width와 height으로 나눠 각각 저장
    i = np.arange(0, img.shape[0], 1)
    j = np.arange(0, img.shape[1], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i * ratioY), np.int32(j * ratioX)
    dst[y,x] = img[i,j]
    return dst

image = cv2.imread("../images/interpolation.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 읽기 에러")

dst1 = scaling(image, (350,400)) #크기 변경 -> 기본 홀이 보이는것이 마치 격자처럼 보인다.forward mapping의 단점.
dst2 = scailing_nearest(image, (350,400)) #크기 변경 -> 최근접 이웃 보간/backward mapping 이용
#forward warping 에서 src 의 좌표를 기준으로 dst 의 좌표를 계산했다면, backward warping 에서는 dst 의 좌표를 기준으로 src 의 좌표를 계산하게 됩니다.
cv2.imshow("Original",image)
cv2.imshow("dst1 -> fowardMapping",dst1)
cv2.imshow("dst2 -> NN interpolation",dst2)

cv2.waitKey(0)
