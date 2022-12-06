import numpy as np,cv2
from Common.utils import contain
from Common.interpolation import bilinear_value

def affine_transform(img,mat):
    rows,cols = img.shape[:2]
    size = img.shape[::-1]
    inv_mat = cv2.invertAffineTransform(mat) #어파인 변환의 역행렬

    dst = np.zeros(img.shape,img.dtype) #목적 영상 생성
    for i in range(rows):
        for j in range(cols):
            pt = np.dot(inv_mat,(j,i,1)) #행렬의 내적 계산
            if contain(pt,size): dst[i,j] = bilinear_value(img,pt) #양선형 보간 수행

    return dst

image = cv2.imread("../images/affine.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

center = (200,200)
angle, scale = 30,1
size = image.shape[::-1] #크기는 shape(height,width)의 역순

pt1 = np.array([(30,70),(20,240),(300,110)],np.float32)
pt2 = np.array([(120,20),(10,180),(280,260)],np.float32)
aff_mat = cv2.getAffineTransform(pt1,pt2) #3개 좌표쌍 어파인 행렬 생성
#getAffineTransform함수는 변환 전의 좌표 3개와 변환 후의 좌표3개를 지정하면 해당 변환을 수행해주는 어파인 행렬을 반환함
rot_mat = cv2.getRotationMatrix2D(center,angle,scale) #어파인 행렬
#getRotationMatrix2D는 회전 변화과 크기변경을 수행하는 어파인 행렬을 반환함

dst1 = affine_transform(image,aff_mat)
dst2 = affine_transform(image,rot_mat)
#직접 구현한 함수로 3개 좌표쌍을 통한 어파인 변환과 회전 변환 행렬을 적용해서 회전 변환을 수행.

image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
dst1 = cv2.cvtColor(dst1,cv2.COLOR_GRAY2BGR)

for i in range(len(pt1)):
    cv2.circle(image,tuple(pt1[i].astype(int)),3,(0,0,255),2)
    cv2.circle(dst1, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)

cv2.imshow("Original",image)
cv2.imshow("dst1_affine",dst1)
cv2.imshow("dst2_affine_rotate",dst2)
cv2.waitKey(0)
