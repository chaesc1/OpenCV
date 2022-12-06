import cv2
import numpy as np

img = cv2.imread("../lenna.png")#이미지 읽어오고
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #흑백 처리
height,width = gray.shape

h = np.zeros(gray.shape,dtype=np.uint8)
diff = np.zeros(gray.shape,dtype=np.uint8) #결과를 담을 빈 배열 생성
#유사 연산자 기법은 center를 기준으로 8방향의 모든 화소와 뺄셈을 시행함
#그중에서 가장 큰 값을 출력화소에 저장한다.
for i in range(height):#자기 자신 좌표를 기준으로 -1,0,1만큼 더하여 계산
    for j in range(width):
        a = []#중앙의 포인트 값을 뺸 것에 절대값을 취한 값들이 들어감.
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if x==0 and y==0: #자기자신 제외.
                    continue
                try:# [i, j]가 [0, 0]인 경우 [x, y]가 [-1, -1]이 되면 계산하는 좌표가 [-1, -1]을 찾게 되며, 이는 계산 에러가 납니다
                    center = int(gray[i][j])
                    m = int(gray[i+x][j+y])
                    a.append(abs(center - m))
                except:
                    continue
                h[i][j] = max(a)
#차연산자 기법은 원래의 화소는 계산에 포함시키지 않는다.
for i in range(height):
    for j in range(width):
        a = []
        for k in [-1, 0, 1]:
            try:
                b = int(abs(gray[i - 1][j - k]))
                c = int(abs(gray[i + 1][j + k]))
                a.append(abs(b - c))
            except:
                continue
        try:
            b = int(abs(gray[i][j - 1]))
            c = int(abs(gray[i][j + 1]))
            a.append(abs(b - c))
        except:
            continue
        diff[i][j] = max(a)
cv2.imshow('original',gray)
cv2.imshow('homo',h)
cv2.imshow('diff',diff)
cv2.waitKey(0)