import numpy as np,cv2
from Common.interpolation import bilinear_value
from Common.utils import contain #사각형으로 범위 확인하는 함수

def contain(p, shape):                              # 좌표(y,x)가 범위내 인지 검사
    return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

def rotate(img,degree): #원점 기준 회전 변환 함수
    dst = np.zeros(img.shape[:2],img.dtype) #목적 영상 생성
    radian = (degree/180) * np.pi #회전각도를 라디안으로.
    sin,cos = np.sin(radian),np.cos(radian)

    # x = x'*cos + y'*sin , y = -x'*sin + y'*cos
    for i in range(img.shape[0]):#역방향 사상 height,y
        for j in range(img.shape[1]): #width,x
            y = -j*sin + i*cos
            x = j*cos + i*sin

            if contain((y,x), img.shape): #입력영상의 범위를 확인
                dst[i,j] = bilinear_value(img,[x,y])

    return dst

def rotate_pt(img,degree,pt): #포인트 기준 회전변환함수
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin,cos = np.sin(radian),np.cos(radian)

    for i in range(img.shape[0]):  # 역방향 사상 height,y
        for j in range(img.shape[1]):  # width,x
            jj,ii = np.subtract((j,i),pt) #전달 받은 좌표만큼 빼서 평행이동을 먼저 수행
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x,y = np.add((x,y),pt) #좌표를 다시 더해서 원래 좌표로 돌아가도록 역 평행이동 수행

            if contain((y,x), img.shape): #입력영상의 범위를 확인
                dst[i,j] = bilinear_value(img,[x,y])
    return dst

image = cv2.imread("../images/rotate.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 읽기 에러")

center = np.divmod(image.shape[::-1],2)[0]
#회전의 기준점으로 입력 영상의 중심점을 계산하여 center객체에 저장.
#행렬의 형태를 역순으로 가져오면 크기가 되고/ divmod함수로 2로 나눈 몫만 가져옴
dst1 = rotate(image,45) #45도
dst2 = rotate(image,-30) #-30도

dst3 = rotate_pt(image,45,center)#center기준
dst4 = rotate_pt(image,-30,center)#center기준
cv2.imshow("Original",image)
cv2.imshow("45degree",dst1)
cv2.imshow("-30degree",dst2)
cv2.imshow("center_45degree",dst3)
cv2.imshow("center_-30degree",dst4)
cv2.waitKey(0)




