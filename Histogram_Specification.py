import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
target = cv2.imread("peppers.png") #원하는 히스토그램을 가진 이미지
target_gray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)

shape = gray.shape #어떤 형식의 배열인지 확인
original = gray.ravel()
specified = target_gray.ravel()

s_values,bin_idx,s_counts = np.unique(original,return_inverse=True,return_counts=True)
#예를 들어 [5, 1, 2, 4, 5, 2, 2]라는 배열(리스트)이 있다면, 이를 unique함수에 넣으면 [1, 2, 4, 5]가 반환되는 형식
#이 unique함수에는 여러 인자가 같이 붙을 수 있는데
# return_inverse가 True라면 반환 값에 원래의 위치에 해당하는 값이 반환됩니다.
# 예를 들어 위에서 [1, 2, 4, 5]가 반환되었을 때, return_inverse=True가 있었다면, [3, 0, 1, 2, 3, 1, 1]이 같이 반환되는 형식입니다.
# 이 값이 있다면 1:1 매칭을 통해 다시 원래의 배열을 만들 수 있는 겁니다.
#return_counts함수가 True라면 반환 값에 각 원소가 몇 개가 있었는지를 반환해줍니다.
# 위의 값에서 [1, 2, 4, 5]가 반환되었을 때, [1, 3, 1, 2]가 같이 반환되는 형식으로 입니다.

t_values,t_counts = np.unique(specified,return_counts=True)

#각 값들을 정규화된 누적합으로 바꾸어주는 과정. cumsum함수를 통해 각원소의 개수의 누적합을 계산
#그중 가장 큰값 즉 배열의 마지막 값으로 나누어 준다.
#그후 255를 곱해 정규화하고 arounds함수를 통해 0.5를 기준으로 소수를 반올림한다. 역평활화는 가장 가까운 수로 바꿔 줘야하기때문
s_quantiles = np.cumsum(s_counts).astype(np.float64)
s_quantiles /= s_quantiles[-1]#배열 마지막 값으로 나눠.(가장 큰값)
sour = np.around(s_quantiles * 255)
t_quantiles = np.cumsum(t_counts).astype(np.float64)
t_quantiles /= t_quantiles[-1]
temp = np.around(t_quantiles * 255)#원하는 타깃영상의 누적합.

b = []

for data in sour:
    diff = temp - data #타깃영상에서 원본영상의 값을 뺀 diff
    mask = np.ma.less_equal(diff,-1)#-1 이하인 값들을 마스크 처리해라.
    print(mask)#마스크 처리가 될 부분(음수)은 True 마스크 처리되지 않을 부분을 False처리
    #마스크는 계산에서 제외되는 부분을 말함.
    if np.all(mask):#배열이 전부 True인지 판별 전부 음수면 if문 실행.
        #즉 모든 diff값이 음수인지 판별.
        c = np.abs(diff).argmin()#diff모든 값들을 절댓값 처리
        b.append(c)#가장 작은 값을 c에 저장후 b배열에 append
        #만약 diff가 모두 음수라면 절대값을 취했을때 가장작은 값이 무엇인지생각하면.
        #가장 작은 값은 원래 diff의 맨 마지막 값.
    masked_diff = np.ma.masked_array(diff,mask)#masked_array -> 마스크를 통해 새로운 배열을 만드는 함수.
    b.append(masked_diff.argmin())

LUT = np.array(b, dtype='uint8')
#원본영상과 타깃영상의 누적 합의 차이로 LUT를 만드는 방법.
out = np.array(LUT[bin_idx].reshape(shape))

cv2.imshow('original',gray)
cv2.imshow('target',target_gray)
cv2.imshow('out',out)

plt.figure()
plt.subplot(1,3,1)
plt.hist(img.ravel(),256,[0,256])
plt.subplot(1,3,2)
plt.hist(target.ravel(),256,[0,256])
plt.subplot(1,3,3)
plt.hist(out.ravel(),256,[0,256])
plt.show()