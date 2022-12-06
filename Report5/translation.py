import numpy as np,cv2

#최상단 왼쪽 원점에서 가로방향만큼 dx,세로 방향만큼 dy만큼 전체 영상의 모든 화소를 이동시키는것
#옮겨진 후에 입력 영상의 범위를 벗어나는 부분은 목적 영상에서 제거시킴.
#또한 평행이동할 화소가 없는 부분인 상단과 왼쪽부분은 0(검은색) 또는 255(흰색)으로 지정한다.

def contain(p, shape):                              # 좌표(y,x)가 범위내 인지 검사
    return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

def translate(img,pt):
    dst = np.zeros(img.shape,img.dtype)
    for i in range(img.shape[0]):#height
        for j in range(img.shape[1]): #width
            x, y = np.subtract((j,i),pt) #좌표는 가로,세로 순서.
            #영상좌표(j,i) 에서 pt좌표 만큼을 빼서 입력 영상 좌표를 계산.-> 역방향 사상 방법 적용
            if contain((y,x),img.shape): #영상범위 확인
                dst[i,j] = img[y,x]
    return dst

image = cv2.imread("../images/translate.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 읽기 에러")

dst1 = translate(image,(30,80))
dst2 = translate(image,(-70,-50))

cv2.imshow("Original",image)
cv2.imshow("30,80",dst1)
cv2.imshow("-70,-50",dst2)
cv2.waitKey(0)