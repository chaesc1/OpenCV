import numpy as np,cv2

def bilinear_value(img,pt):#단일 화소 양선형 보간 수행함수
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x - 1 #영상 범위를 벗어 났을때
    if y >= img.shape[0]-1: y = y - 1

    P1 = float(img[y,x]) #좌상단 좌표
    P2 = float(img[y+0, x+1])  # 우상단 좌표
    P3 = float(img[y+1, x+0])  # 좌하단 좌표
    P4 = float(img[y+1, x+1])  # 우하단 좌표

    alpha, beta = pt[1] - y, pt[0] - x #거리 비율 알파,베타
    M1 = P1 + alpha * (P3 - P1) #1차 보간
    M2 = P2 + alpha * (P4 - P2)

    P = M1 + beta * (M2 - M1) #2차 보간
    return np.clip(P, 0, 255) #클립함수를 사용하여 화소값을 0-255로 유지한다.
    #array 내의 element들에 대해서
    #min 값 보다 작은 값들을 min값으로 바꿔주고
    #max 값 보다 큰 값들을 max값으로 바꿔주는 함수.

#양선형 보간법 수행 함수
def scaling_bilinear(img,size):
    ratioY,ratioX = np.divide(size[::-1],img.shape[:2]) #변경 크기 비율/ size를 width와 height으로 나눠 각각 저장

    dst = [[bilinear_value(img, (j / ratioX, i / ratioY))  # for문 이용한 리스트 생성
            for j in range(size[0])]
           for i in range(size[1])]
    #목적영상의 모든 화소를 순회하여 한좌표씩 양선형 보간을 실시
    return np.array(dst, img.dtype)

image = cv2.imread("../lenna.png",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상읽기오류")

size = (1024,1024) #기ㅈ존 영상(512*512)의 2배로 늘려보자
dst1 = scaling_bilinear(image, size) #양선형 보간
dst2 = cv2.resize(image,size,0,0,cv2.INTER_LINEAR) #opencv함수를 이용한 양선형 보간

cv2.imshow("Original",image)
cv2.imshow("Bilinear_USER",dst1)
cv2.imshow("OpenCV Bilinear",dst2)
cv2.waitKey(0)
